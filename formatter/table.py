from sly import Lexer


def _(*args):
    return _


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

    @_(r"(\".*\")|('.*')")
    def STRING(self, token):
        return token

    @_(r"[dD][eE][fF][iI][nN][eE] [tT][aA][bB][lL][eE]")
    def DEFINE(self, token):
        return token

    @_(r"[sS][cC][hH][eE][mM][aA]([fF][uU][lL][lL]|[lL][eE][sS][sS])")
    def SCHEMA(self, token):
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

    @_(r";")
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
        tokens = list(TableLexer().tokenize(text))
        formatted: str = ""
        for token in tokens:
            formatted += cls.BEFORE_TYPE.get(token.type, "")
            formatted += cls.BEFORE_VALUE.get(token.value.upper(), "")
            formatted += token.value
            formatted += cls.AFTER_TYPE.get(token.type, "")
            formatted += cls.AFTER_VALUE.get(token.value.upper(), "")
        return formatted
