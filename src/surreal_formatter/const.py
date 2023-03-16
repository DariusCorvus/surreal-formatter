OPERATORS = (
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
    r"<",
    r">=",
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

COMMENT = (r"/\*\n*.*\n*\*/", r"--.*", r"//.*", r"#.*")

PARAMETER = (r"\$[_0-9a-zA-Z]+",)

WHERE = (r"[wW][hH][eE][rR][eE]",)

FOR = (r"[fF][oO][rR]",)

PERMISSIONS = (r"[pP][eE][rR][mM][iI][sS][sS][iI][oO][nN][sS]",)

STRING = (r"(\"|')(.*|\n*)(\"|')",)

ON = (r"[oO][nN]",)

REGEX = (r"/.*/",)

LET_VALUE = (r"\$value",)

ASSERT = (r"[aA][sS][sS][eE][rR][tT]",)

STATEMENT_WITH_SEPERATORS = (
    r"([sS][eE][lL][eE][cC][tT]|[cC][rR][eE][aA][tT][eE]|[uU][pP][dD][aA][tT][eE]|[dD][eE][lL][eE][tT][eE]),",
)

STATEMENTS = (
    r"([sS][eE][lL][eE][cC][tT]|[cC][rR][eE][aA][tT][eE]|[uU][pP][dD][aA][tT][eE]|[dD][eE][lL][eE][tT][eE])",
)

TABLE = (r"[_a-zA-Z0-9]+",)

SEPERATOR = (r",",)

DOT = (r"\.",)

ARRAY_ASTERISK = (r"\[\*\]",)

FUNCTION = (r"(\w*(::)?)+\(.*\)",)

EOQ = (r";",)
