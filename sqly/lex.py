import ply.lex as lex, 
from ply.lex import TOKEN


literals = "()"

reserved = {
    "SELECT": "SELECT",
    "DISTINCT": "DISTINCT",
    "ALL": "ALL",
    "FROM": "FROM",
    "WHERE": "WHERE",
    "NOT": "NOT",
    "NULL": "NULL",
    "DEFAULT": "DEFAULT",
}

tokens = [
    "SEPARATOR",
    "PUNCTUATION_MARK",
    "DIGIT",
    "CHAR",
    "NUMBER",
    "SYMBOL",
    "STRING",
    "ID",
    "TABLE_NAME",
    "FIELD_NAME",
    "NUMERICAL_OPERATOR",
    "NUMERICAL_FACTOR",
    "NUMERICAL_EXPRESSION",
    "VALUE",
    "COMPARSION_OPERATOR",
    "CONDITIONAL_OPERATOR",
    "FIELD_VALUE",
    "PREDICATE",
    "CONDITIONAL_FACTOR",
    "CONDITIONAL",
    "FIELD_LIST",
]

tokens += reserved.values()

t_SEPARATOR = r"(\s)"
t_PUNCTUATION_MARK = r"[\.,!?:;]"
t_DIGIT = r"\d"
t_CHAR = r"[A-Z]"
t_NUMBER = f"(-?{t_DIGIT}+.?{t_DIGIT}*)"
t_SYMBOL = f"({t_DIGIT}|{t_CHAR}|{t_PUNCTUATION_MARK}|{t_SEPARATOR})"
t_STRING = f'"{t_SYMBOL}*"'
t_NUMERICAL_OPERATOR = r"[+\-*/]"
t_COMPARSION_OPERATOR = r"(<>|<=|>=|<|>|=)"
identifier = f"({t_CHAR}|_)({t_CHAR}|_|{t_DIGIT})*"


def t_CONDITIONAL_OPERATOR(t):
    r"(AND|OR)"
    return t

@TOKEN(identifier)
def t_ID(t):
    t.type = reserved.get(t.value, "ID")
    return t


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


def t_error(t):
    print(
        f"Illegal character '{t.value[0]}' on line {t.lineno} "
        f"column {find_column(t.lexer.lexdata, t)}"
    )
    t.lexer.skip(1)


def find_column(input, token):
    line_start = input.rfind("\n", 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


# Build the lexer
lexer = lex.lex(debug=True)

if __name__ == "__main__":
    lex.runmain()
