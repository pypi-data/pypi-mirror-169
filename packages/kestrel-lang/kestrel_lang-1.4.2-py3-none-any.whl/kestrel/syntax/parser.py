import ast
from datetime import datetime, timedelta
from pkgutil import get_data

from firepit.query import BinnedColumn, Filter, Predicate
from firepit.timestamp import timefmt
from lark import Lark, Token, Transformer, Tree


def parse(stmts, default_variable="_", default_sort_order="desc"):
    # the public parsing interface for Kestrel
    # return abstract syntax tree
    # check kestrel.lark for details
    grammar = get_data(__name__, "kestrel.lark").decode("utf-8")
    return Lark(
        grammar,
        parser="lalr",
        transformer=_PostParsing(default_variable, default_sort_order),
    ).parse(stmts)


def get_all_input_var_names(stmt):
    input_refs = ["input", "input_2", "variablesource"]
    inputs_refs = stmt["inputs"] if "inputs" in stmt else []
    return [stmt.get(k) for k in input_refs if k in stmt] + inputs_refs


################################################################
#                           Private
################################################################


class _PostParsing(Transformer):
    def __init__(self, default_variable, default_sort_order):
        self.default_variable = default_variable
        self.default_sort_order = default_sort_order
        super().__init__()

    def start(self, args):
        return args

    def statement(self, args):
        # Kestrel syntax: a statement can only has one command
        stmt = args.pop()
        return stmt

    def assignment(self, args):
        stmt = args[1] if len(args) == 2 else args[0]
        stmt["output"] = _extract_var(args, self.default_variable)
        return stmt

    def assign(self, args):
        result = args[0]  # Already transformed in expression method below
        result["command"] = "assign"
        return result

    def merge(self, args):
        return {
            "command": "merge",
            "inputs": _extract_vars(args, self.default_variable),
        }

    def info(self, args):
        return {"command": "info", "input": _extract_var(args, self.default_variable)}

    def disp(self, args):
        result = {"command": "disp"}
        for arg in args:
            if isinstance(arg, dict):
                result.update(arg)
        if "attrs" not in result:
            result["attrs"] = "*"
        return result

    def get(self, args):
        datasource = _extract_datasource(args)
        packet = {
            "command": "get",
            "type": _extract_entity_type(args),
            "patternbody": _assert_and_extract_single("STIXPATTERNBODY", args),
        }
        if datasource:
            packet["datasource"] = datasource

        time_range = {}
        for item in args:
            if isinstance(item, dict):
                time_range.update(item)

        if "start" in time_range and "stop" in time_range:
            packet["timerange"] = (time_range["start"], time_range["stop"])
        else:
            packet["timerange"] = None

        return packet

    def find(self, args):
        packet = {
            "command": "find",
            "type": _extract_entity_type(args),
            "relation": _assert_and_extract_single("RELATION", args).lower(),
            "reversed": _extract_if_reversed(args),
            "input": _extract_var(args, self.default_variable),
        }

        time_range = {}
        for item in args:
            if isinstance(item, dict):
                time_range.update(item)

        if "start" in time_range and "stop" in time_range:
            packet["timerange"] = (time_range["start"], time_range["stop"])
        else:
            packet["timerange"] = None

        return packet

    def join(self, args):
        if len(args) == 5:
            return {
                "command": "join",
                "input": _first(args),
                "input_2": _second(args),
                "path": _fourth(args),
                "path_2": _fifth(args),
            }
        else:
            return {"command": "join", "input": _first(args), "input_2": _second(args)}

    def group(self, args):
        # args[1] was already transformed by path_list/valuelist
        cols = args[2]
        result = {
            "command": "group",
            "paths": cols,
            "input": _extract_var(args, self.default_variable),
        }
        aggregations = args[3] if len(args) > 3 else None
        if aggregations:
            result["aggregations"] = aggregations
        return result

    def sort(self, args):
        return {
            "command": "sort",
            "path": _extract_stixpath(args),
            "input": _extract_var(args, self.default_variable),
            "ascending": _extract_direction(args, self.default_sort_order),
        }

    def apply(self, args):
        input_vars = []
        for arg in args:
            if isinstance(arg, dict) and "variables" in arg:
                input_vars = arg["variables"]
                break
        return {
            "command": "apply",
            "workflow": _first(args),
            "inputs": input_vars,
            "parameter": _merge_args("anaparams", args),
        }

    def load(self, args):
        return {
            "command": "load",
            "type": _extract_entity_type(args),
            "path": _extract_dumppath(args),
        }

    def save(self, args):
        return {
            "command": "save",
            "input": _extract_var(args, self.default_variable),
            "path": _extract_dumppath(args),
        }

    def new(self, args):
        return {
            "command": "new",
            "type": _extract_entity_type(args),
            "data": _assert_and_extract_single("VARDATA", args),
        }

    def expression(self, args):
        result = args[0]
        for arg in args:
            result.update(arg)
        return result

    def transform(self, args):
        return {
            "input": _extract_var(args, self.default_variable),
            "transform": _assert_and_extract_single("TRANSFORM", args),
        }

    def where_clause(self, args):
        return {
            "where": Filter([args[0]]),
        }

    def attr_clause(self, args):
        paths = _assert_and_extract_single("STIXPATHS", args)
        return {
            "attrs": paths if paths else "*",
        }

    def sort_clause(self, args):
        return {
            "path": _extract_stixpath(args),
            "ascending": _extract_direction(args, self.default_sort_order),
        }

    def limit_clause(self, args):
        return {
            "limit": _extract_int(args),
        }

    def offset_clause(self, args):
        return {
            "offset": _extract_int(args),
        }

    def timespan(self, args):
        result = {}
        for arg in args:
            result.update(arg)
        return result

    def relative_timespan(self, args):
        # args should be num and unit
        num = int(_first(args))
        unit = _second(args).lower()
        if unit in ("days", "d"):
            delta = timedelta(days=num)
        elif unit in ("hours", "h"):
            delta = timedelta(hours=num)
        elif unit in ("minutes", "m"):
            delta = timedelta(minutes=num)
        elif unit in ("seconds", "s"):
            delta = timedelta(seconds=num)
        stop = datetime.utcnow()
        start = stop - delta
        return {"start": timefmt(start, prec=6), "stop": timefmt(stop, prec=6)}

    def starttime(self, args):
        return {"start": _assert_and_extract_single("ISOTIMESTAMP", args)}

    def endtime(self, args):
        return {"stop": _assert_and_extract_single("ISOTIMESTAMP", args)}

    def variables(self, args):
        return {"variables": _extract_vars(args, self.default_variable)}

    def localargs(self, args):
        return {args[0].value: args[1]}

    def valuelist(self, args):
        if len(args) == 1:
            return args[0].value
        elif len(args) > 1:
            return [arg.value for arg in args]
        return None

    def number(self, args):
        return {args[0].value: ast.literal_eval(args[1].value)}

    def grp_spec(self, args):
        return args

    def grp_expr(self, args):
        path = args[0]
        if isinstance(path, str):
            path = _normalize_paths(path)[0]
        return path

    def bin_func(self, args):
        path = args[0].value
        num = int(args[1].value)
        if len(args) >= 3:
            unit = args[2].value
        else:
            unit = None
        alias = f"{path}_bin"
        return BinnedColumn(path, num, unit, alias=alias)

    def agg_list(self, args):
        return [arg for arg in args]

    def agg(self, args):
        func = args[0].value.lower()
        alias = args[2].value if len(args) > 2 else f"{func}_{args[1].value}"
        return {"func": func, "attr": args[1].value, "alias": alias}

    def disj(self, args):
        lhs = str(args[0]) if isinstance(args, Token) else args[0]
        rhs = str(args[1]) if isinstance(args, Token) else args[1]
        return Predicate(lhs, "OR", rhs)

    def conj(self, args):
        lhs = str(args[0]) if isinstance(args, Token) else args[0]
        rhs = str(args[1]) if isinstance(args, Token) else args[1]
        return Predicate(lhs, "AND", rhs)

    def comp(self, args):
        lhs = str(args[0]) if isinstance(args, Token) else args[0]
        op = str(args[1])
        rhs = str(args[2]) if isinstance(args, Token) else args[2]
        return Predicate(lhs, op, rhs)

    def null_comp(self, args):
        lhs = str(args[0])
        op = str(args[1])
        if op == "IS NOT":
            op = "!="
        else:
            op = "="
        rhs = "NULL"
        return Predicate(lhs, op, rhs)

    def column(self, args):
        return args[0].value

    def squoted_str(self, args):
        return args[0].value.strip("'")

    def num_literal(self, args):
        return args[0].value

    def null(self, args):
        return "NULL"


def _first(args):
    return args[0].value


def _second(args):
    return args[1].value


def _third(args):
    return args[2].value


def _fourth(args):
    return args[3].value


def _fifth(args):
    return args[4].value


def _last(args):
    return args[-1].value


def _assert_and_extract_single(arg_type, args):
    items = [arg.value for arg in args if hasattr(arg, "type") and arg.type == arg_type]
    assert len(items) <= 1
    return items.pop() if items else None


def _extract_int(args):
    value = _assert_and_extract_single("INT", args)
    return int(value) if value else None


def _extract_var(args, default_variable):
    # extract a single variable from the args
    # default variable if no variable is found
    v = _assert_and_extract_single("VARIABLE", args)
    return v if v else default_variable


def _extract_vars(args, default_variable):
    var_names = []
    for arg in args:
        if hasattr(arg, "type") and arg.type == "VARIABLE":
            var_names.append(arg.value)
    if not var_names:
        var_names = [default_variable]
    return var_names


def _extract_stixpath(args):
    # extract a single stix path from the args
    return _assert_and_extract_single("STIXPATH", args)


def _extract_datasource(args):
    raw_ds = _assert_and_extract_single("DATASRC", args)
    ds = raw_ds.strip('"') if raw_ds else None
    return ds


def _extract_entity_type(args):
    # extract a single entity type from the args
    return _assert_and_extract_single("ENTITY_TYPE", args)


def _extract_dumppath(args):
    # extract a single stix path from the args
    return _assert_and_extract_single("DUMPPATH", args)


def _extract_direction(args, default_sort_order):
    # extract sort direction from args
    # default direction if no variable is found
    # return: if descending
    ds = [
        x for x in args if hasattr(x, "type") and (x.type == "ASC" or x.type == "DESC")
    ]
    assert len(ds) <= 1
    d = ds.pop().type if ds else default_sort_order
    return True if d == "ASC" else False


def _extract_if_reversed(args):
    rs = [x for x in args if hasattr(x, "type") and x.type == "REVERSED"]
    return True if rs else False


def _merge_args(arg_type, args):
    items = dict()
    for arg in args:
        if not isinstance(arg, Tree) or not hasattr(arg, "data"):
            continue
        if arg.data != arg_type:
            continue
        for t in arg.children:
            items.update(t)
    return items


def _normalize_paths(stixpaths):
    if isinstance(stixpaths, str):
        stixpaths = [stixpaths]
    # Sanitize paths
    cols = []
    for stixpath in stixpaths:
        sco_type, _, prop = stixpath.rpartition(":")
        # We should probably verify sco_type here
        cols.append(prop)
    return cols
