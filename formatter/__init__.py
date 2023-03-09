from .query import QueryLexer
from .table import DefineTableLexer


def _parse_default(text: str) -> str:
    return text + "\n"


def _none(*args) -> str:
    args = args
    return ""


PARSER = {
    "COMMENT": _parse_default,
    "SELECT": _parse_default,
    "DEFINE_TABLE": DefineTableLexer.parse,
}


def parse(text: str) -> str:
    querys = list(QueryLexer().tokenize(text))
    result: str = ""
    for query in querys:
        result += PARSER.get(query.type, _none)(query.value)
    return result
