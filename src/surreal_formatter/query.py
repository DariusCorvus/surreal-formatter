from sly import Lexer

from surreal_formatter import const
from surreal_formatter.helper import _


class QueryLexer(Lexer):
    @_(*const.COMMENT)
    def COMMENT(self, token):
        return token

    @_(r"[dD][eE][fF][iI][nN][eE] [tT][aA][bB][lL][eE]((.|\n)+);{0,1}")
    def DEFINE_TABLE(self, token):
        return token

    @_(r"[dD][eE][fF][iI][nN][eE] [fF][iI][eE][lL][dD]((.|\n)+);{0,1}")
    def DEFINE_FIELD(self, token):
        return token

    @_(r"[lL][eE][tT] $.*;{0,1}")
    def LET(self, token):
        return token

    @_(r"[sS][eE][lL][eE][cC][tT].+;{0,1}")
    def SELECT(self, token):
        return token

    @_(r"[iI][nN][sS][eE][rR][tT].+;{0,1}")
    def INSERT(self, token):
        return token

    @_(r"[cC][rR][eE][aA][tT][eE].+;{0,1}")
    def CREATE(self, token):
        return token

    @_(r"[uU][pP][dD][aA][tT][eE].+;{0,1}")
    def UPDATE(self, token):
        return token

    @_(r"[rR][eE][lL][aA][tT][eE].+;{0,1}")
    def RELATE(self, token):
        return token

    @_(r"[dD][eE][lL][eE][tT][eE].+;{0,1}")
    def DELETE(self, token):
        return token

    @_(r"[\n\t .]")
    def IGNORE(self, token):
        token = token
        ...

    tokens = {
        COMMENT,
        DEFINE_TABLE,
        DEFINE_FIELD,
        LET,
        SELECT,
        INSERT,
        CREATE,
        UPDATE,
        RELATE,
        DELETE,
        IGNORE,
    }
