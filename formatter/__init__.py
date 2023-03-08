from .query import QueryLexer
from .table import DefineTableLexer

PARSER = {"COMMENT": print, "SELECT": print, "DEFINE_TABLE": DefineTableLexer.parse}


def parse(text: str) -> str:
  querys = list(QueryLexer().tokenize(text))
  for query in querys:
    PARSER.get(query.type, lambda _: ...)(query.value)
