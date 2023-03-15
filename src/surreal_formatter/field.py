from typing import Protocol

from sly import Lexer


class Token(Protocol):
    type: str
    value: str


def _(*args):
    args = args
    return _


def upper(token: Token) -> Token:
    token.value = token.value.upper()
    return token


def lower(token: Token) -> Token:
    token.value = token.value.lower()
    return token


class FieldLexer(Lexer):
    ignore_newline = r"\n+"
    ignore_whitespace = r" "
    ignore_tab = r"\t"

    literals = {"(", ")", "[", "]", "{", "}"}

    @_(r"(\".*\")|('.*')")
    def STRING(self, token):
        return token

    @_(r"[dD][eE][fF][iI][nN][eE] [fF][iI][eE][lL][dD]")
    def DEFINE(self, token: Token):
        token = upper(token)
        return token

    @_(r"[oO][nN]")
    def ON(self, token: Token):
        token = upper(token)
        return token

    @_(r"[tT][yY][pP][eE]")
    def TYPE(self, token: Token):
        token = upper(token)
        return token

    @_(r"[aA][nN][yY]")
    def TYPE_ANY(self, token: Token):
        token = lower(token)
        return token

    @_(r"[aA][rR][rR][aA][yY]")
    def TYPE_ARRAY(self, token: Token):
        token = lower(token)
        return token

    @_(r"[bB][oO][oO][lL]")
    def TYPE_BOOL(self, token: Token):
        token = lower(token)
        return token

    @_(r"[dD][aA][tT][eE][tT][iI][mM][eE]")
    def TYPE_DATETIME(self, token: Token):
        token = lower(token)
        return token

    @_(r"[dD][eE][cC][iI][mM][aA][lL]")
    def TYPE_DECIMAL(self, token: Token):
        token = lower(token)
        return token

    @_(r"[fF][lL][oO][aA][tT]")
    def TYPE_FLOAT(self, token: Token):
        token = lower(token)
        return token

    @_(r"[iI][nN][tT]")
    def TYPE_INT(self, token: Token):
        token = lower(token)
        return token

    @_(r"[nN][uU][mM][bB][eE][rR]")
    def TYPE_NUMBER(self, token: Token):
        token = lower(token)
        return token

    @_(r"[oO][bB][jJ][eE][cC][tT]")
    def TYPE_OBJECT(self, token: Token):
        token = lower(token)
        return token

    @_(r"[sS][tT][rR][iI][nN][gG]")
    def TYPE_STRING(self, token: Token):
        token = lower(token)
        return token

    @_(r"[rR][eE][cC][oO][rR][dD]")
    def TYPE_RECORD(self, token: Token):
        token = lower(token)
        return token

    @_(
        r"[gG][eE][oO][mM][eE][tT][rR][yY](\((([fF][eE][aA][tT][uU][rR][eE]|[pP][oO][iI][nN][tT]|[lL][iI][nN][eE]|[pP][oO][lL][yY][gG][oO][nN]|[mM][uU][lL][tT][iI][pP][oO][iI][nN][tT]|[mM][uU][lL][tT][iI][lL][iI][nN][eE]|[mM][uU][lL][tT][iI][pP][oO][lL][yY][gG][oO][nN]|[cC][oO][lL][lL][eE][cC][tT][iI][oO][nN]),?)+\)){0,1}"
    )
    def TYPE_GEOMETRY(self, token: Token):
        token = lower(token)
        return token

    @_(r"[aA][sS][sS][eE][rR][tT]")
    def ASSERT(self, token: Token):
        token = upper(token)
        return token

    @_(r"\$value")
    def PARAM_VALUE(self, token: Token):
        return token

    @_(r"/.*/")
    def REGEX(self, token: Token):
        return token

    @_(
        r"=",
        r"!=",
        r"==",
        r"\?=",
        r"\*=",
        r"~",
        r"!~",
        r"\?~",
        r"\*~",
        r"<",
        r"<=",
        r">",
        r">=",
        r"\+",
        r"-",
        r"\*",
        r"/",
        r"&&",
        r"\|\|",
        r"AND",
        r"OR",
        r"IS",
        r"IS NOT",
        r"(CONTAINS|∋)",
        r"(CONTAINSNOT|∌)",
        r"(CONTAINSALL|⊇)",
        r"(CONTAINSANY|⊃)",
        r"(CONTAINSNONE|⊅)",
        r"(INSIDE|∈)",
        r"(NOTINSIDE|∉)",
        r"(ALLINSIDE|⊆)",
        r"(ANYINSIDE|⊂)",
        r"(NONEINSIDE|⊄)",
        r"OUTSIDE",
        r"INTERSECTS",
    )
    def OPERATOR(self, token):
        token = upper(token)
        return token

    @_(r"(\w*(::)?)+\(.*\)")
    def FUNCTION(self, token):
        return token

    @_(r"[pP][eE][rR][mM][iI][sS][sS][iI][oO][nN][sS]")
    def PERMISSIONS(self, token):
        return token

    @_(r"[fF][oO][rR]")
    def FOR(self, token):
        return token

    @_(
        r"([sS][eE][lL][eE][cC][tT]|[cC][rR][eE][aA][tT][eE]|[uU][pP][dD][aA][tT][eE]|[dD][eE][lL][eE][tT][eE]),"
    )
    def STATEMENT_WITH_SEPERATOR(self, token):
        return token

    @_(
        r"([sS][eE][lL][eE][cC][tT]|[cC][rR][eE][aA][tT][eE]|[uU][pP][dD][aA][tT][eE]|[dD][eE][lL][eE][tT][eE])"
    )
    def STATEMENT(self, token):
        return token

    @_(r"[wW][hH][eE][rR][eE]")
    def WHERE(self, token):
        return token

    @_(r"[_a-zA-Z0-9]+")
    def TABLE(self, token):
        return token

    @_(r",")
    def SEPERATOR(self, token):
        return token

    @_(r"\.")
    def DOT(self, token):
        return token

    @_(r"\$[_0-9a-zA-Z]+")
    def PARAMETER(self, token):
        return token

    @_(r"\[\*\]")
    def ASTERISK(self, token):
        return token

    @_(r";")
    def EOQ(self, token: Token):
        return token

    tokens = {
        STRING,
        DEFINE,
        ON,
        TYPE,
        TYPE_ANY,
        TYPE_ARRAY,
        TYPE_BOOL,
        TYPE_DATETIME,
        TYPE_DECIMAL,
        TYPE_FLOAT,
        TYPE_INT,
        TYPE_NUMBER,
        TYPE_OBJECT,
        TYPE_STRING,
        TYPE_RECORD,
        TYPE_GEOMETRY,
        ASSERT,
        PARAM_VALUE,
        REGEX,
        OPERATOR,
        FUNCTION,
        PERMISSIONS,
        FOR,
        STATEMENT_WITH_SEPERATOR,
        STATEMENT,
        WHERE,
        TABLE,
        SEPERATOR,
        DOT,
        PARAMETER,
        EOQ,
    }

    BEFORE_TYPE = {
        "ON": " ",
        "TYPE": " ",
        "EOQ": "\n",
        "OPERATOR": " ",
        "ASSERT": " ",
        "PERMISSIONS": "\n\t",
        "FOR": "\n\t\t",
        "STATEMENT_WITH_SEPERATOR": " ",
        "STATEMENT": " ",
    }
    BEFORE_VALUE = {}
    AFTER_TYPE = {
        "PERMISSIONS": " ",
        "WHERE": " ",
        "STATEMENT": "\n\t\t\t",
        "DEFINE": " ",
        "ON": " ",
        "TYPE": " ",
        "EOQ": "\n",
        "OPERATOR": " ",
        "ASSERT": "\n\t",
    }
    AFTER_VALUE = {}

    @classmethod
    def parse(cls, text: str) -> str:
        tokens = list(cls().tokenize(text))
        formatted: str = ""

        for token in tokens:
            formatted += cls.BEFORE_TYPE.get(token.type, "")
            formatted += cls.BEFORE_VALUE.get(token.value.upper(), "")
            formatted += token.value
            formatted += cls.AFTER_TYPE.get(token.type, "")
            formatted += cls.AFTER_VALUE.get(token.value.upper(), "")

        return formatted

    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1
