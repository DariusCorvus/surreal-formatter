from sly import Lexer


def _(*args):
    return _


class DefineTableLexer(Lexer):
    COMMENT = r"(--.*)|(//.*)|(#.*)"
    STRING = r"(\".*\")|('.*')"

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

    @_(r"[a-zA-Z]+")
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
        COMMENT,
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

    @staticmethod
    def parse(text):
        tokens = list(DefineTableLexer().tokenize(text))
        for token in tokens:
            print(
                DefineTableLexer.BEFORE_TYPE.get(token.type, ""),
                DefineTableLexer.BEFORE_VALUE.get(token.value.upper(), ""),
                end="",
                sep="",
            )

            print(token.value, end="")

            print(
                DefineTableLexer.AFTER_TYPE.get(token.type, ""),
                DefineTableLexer.AFTER_VALUE.get(token.value.upper(), ""),
                end="",
                sep="",
            )
