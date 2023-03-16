from sly import Lexer

from surreal_formatter.helper import _

from . import const


class TableLexer(Lexer):
    BEFORE_TYPE = {
        "SCHEMA": " \n\t",
        "PERMISSIONS": "\n\t",
        "FOR": "\n\t\t",
        "STATEMENT_WITH_SEPERATOR": " ",
        "STATEMENT": " ",
        "OPERATOR": " ",
        "EOQ": "\n",
    }
    BEFORE_VALUE = {"OR": "\n\t\t\t", "AND": "\n\t\t\t"}

    AFTER_TYPE = {
        "PERMISSIONS": " ",
        "DEFINE": " ",
        "OPERATOR": " ",
        "WHERE": " ",
        "COMMENT": "\n",
        "EOQ": "\n",
        "STATEMENT": "\n\t\t\t",
    }
    AFTER_VALUE = {"OR": " ", "AND": " "}

    ignore_newline = r"\n+"
    ignore_whitespace = r" "
    ignore_tab = r"\t"

    @_(*const.STRING)
    def STRING(self, token):
        return token

    @_(*const.OPERATORS)
    def OPERATOR(self, token):
        return token

    @_(r"[dD][eE][fF][iI][nN][eE] [tT][aA][bB][lL][eE]")
    def DEFINE(self, token):
        return token

    @_(r"[sS][cC][hH][eE][mM][aA]([fF][uU][lL][lL]|[lL][eE][sS][sS])")
    def SCHEMA(self, token):
        return token

    @_(*const.PERMISSIONS)
    def PERMISSIONS(self, token):
        return token

    @_(*const.FOR)
    def FOR(self, token):
        return token

    @_(*const.STATEMENT_WITH_SEPERATORS)
    def STATEMENT_WITH_SEPERATOR(self, token):
        return token

    @_(*const.STATEMENTS)
    def STATEMENT(self, token):
        return token

    @_(*const.WHERE)
    def WHERE(self, token):
        return token

    @_(*const.TABLE)
    def TABLE(self, token):
        return token

    @_(*const.SEPERATOR)
    def SEPERATOR(self, token):
        return token

    @_(*const.DOT)
    def DOT(self, token):
        return token

    @_(*const.PARAMETER)
    def PARAMETER(self, token):
        return token

    @_(*const.EOQ)
    def EOQ(self, token):
        return token

    def ignore_newline(self, t):
        self.lineno += t.value.count("\n")

    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1

    tokens = {
        STRING,
        DEFINE,
        PERMISSIONS,
        FOR,
        STATEMENT_WITH_SEPERATOR,
        STATEMENT,
        WHERE,
        TABLE,
        OPERATOR,
        SEPERATOR,
        DOT,
        PARAMETER,
        SCHEMA,
        EOQ,
    }

    @classmethod
    def parse(cls, text):
        tokens = list(cls().tokenize(text))
        formatted: str = ""
        for token in tokens:
            formatted += cls.BEFORE_TYPE.get(token.type, "")
            formatted += cls.BEFORE_VALUE.get(token.value.upper(), "")
            formatted += token.value
            formatted += cls.AFTER_TYPE.get(token.type, "")
            formatted += cls.AFTER_VALUE.get(token.value.upper(), "")
        return formatted
