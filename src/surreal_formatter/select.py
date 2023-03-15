from sly import Lexer

from config import Config

from .token import Token, upper

config = Config()


def _(*args):
    args = args
    return _


class SelectLexer(Lexer):
    ignore_newline = r"\n+"
    ignore_whitespace = r" "
    ignore_tab = r"\t"

    literals = {"(", ")", "[", "]", "{", "}"}

    @_(r"(\".*\")|('.*')")
    def STRING(self, token: Token):
        return token

    @_(r"[sS][eE][lL][eE][cC][tT]")
    def SELECT(self, token: Token):
        token = upper(token)
        return token

    @_(r",")
    def SEPERATOR(self, token: Token):
        return token

    @_(r"[fF][rR][oO][mM]")
    def FROM(self, token: Token):
        token = upper(token)
        return token

    @_(r"[wW][hH][eE][rR][eE]")
    def WHERE(self, token: Token):
        token = upper(token)
        return token

    @_(r"[oO][rR][dD][eE][rR] [bB][yY]")
    def ORDER_BY(self, token: Token):
        token = upper(token)
        return token

    @_(r"[cC][oO][lL][lL][aA][tT][eE]", r"[nN][uU][mM][eE][rR][iI][cC]")
    def ORDER_TYPE(self, token: Token):
        token = upper(token)
        return token

    @_(r"[aA][sS][cC]", r"[dD][eE][sS][cC]")
    def DIRECTION(self, token: Token):
        token = upper(token)
        return token

    @_(
        r"!=",
        r"==",
        r"\?=",
        r"\*=",
        r"=",
        r"!~",
        r"\?~",
        r"\*~",
        r"~",
        r"<=",
        r">=",
        r"<",
        r">",
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
    def OPERATOR(self, token: Token):
        token = upper(token)
        return token

    @_(r"(\w*(::)?)+\(.*\)")
    def FUNCTION(self, token: Token):
        return token

    @_(r"[lL][iI][mM][iI][tT]")
    def LIMIT(self, token: Token):
        token = upper(token)
        return token

    @_(r"[sS][tT][aA][rR][tT]")
    def START(self, token: Token):
        token = upper(token)
        return token

    @_(r"[fF][eE][tT][cC][hH]")
    def FETCH(self, token: Token):
        token = upper(token)
        return token

    @_(r"[tT][iI][mM][eE][oO][uU][tT]")
    def TIMEOUT(self, token: Token):
        token = upper(token)
        return token

    @_(r"[pP][aA][rR][aA][lL][lL][eE][lL]")
    def PARALLEL(self, token: Token):
        token = upper(token)
        return token

    @_(r"\*", r"[0-9]*[_a-zA-Z]+[0-9]*[_a-zA-Z]+((\.?[0-9]*)[_a-zA-Z]*)+", r"[a-zA-Z]+")
    def FIELD(self, token: Token):
        return token

    @_(r"[0-9]+")
    def NUMBER(self, token: Token):
        return token

    @_(r";")
    def EOQ(self, token: Token):
        return token

    tokens = {
        STRING,
        SELECT,
        SEPERATOR,
        FROM,
        WHERE,
        ORDER_BY,
        ORDER_TYPE,
        DIRECTION,
        OPERATOR,
        FUNCTION,
        LIMIT,
        START,
        FETCH,
        TIMEOUT,
        PARALLEL,
        FIELD,
        NUMBER,
        EOQ,
    }

    BEFORE_TYPE = {
        "FROM": "\n\t",
        "WHERE": "\n\t\t",
        "LIMIT": "\n",
        "START": "\n",
        "EOQ": "\n",
        "OPERATOR": " ",
    }
    BEFORE_VALUE = {"AND": "\n\t\t", "OR": "\n\t\t"}
    AFTER_TYPE = {
        "OPERATOR": " ",
        "FROM": " ",
        "LIMIT": " ",
        "START": " ",
        "SELECT": "\n\t\t",
        "SEPERATOR": "\n\t\t",
        "WHERE": "\t",
        "EOQ": "\n",
    }
    AFTER_VALUE = {"AND": " \t", "OR": "  \t"}

    @classmethod
    def parse(cls, text: str) -> str:
        tokens = list(cls().tokenize(text))
        formatted: str = ""
        for token in tokens:
            formatted += cls.BEFORE_TYPE.get(token.type, "")
            formatted += cls.BEFORE_VALUE.get(token.value.upper(), "")
            formatted += token.value
            if value := cls.AFTER_VALUE.get(token.value.upper(), None):
                formatted += value
            else:
                formatted += cls.AFTER_TYPE.get(token.type, "")

        return formatted

    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1
