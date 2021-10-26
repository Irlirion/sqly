import ply.lex as lex

tokens = [
    "SEPARATOR",
    "PUNCTUATION_MARK",
    "DIGIT",
    "CHAR",
    "NUMBER",
    "SYMBOL",
    "STRING",
    "ID",
    "NUMERICAL_OPERATOR",
    "NUMERICAL_FACTOR",
    "t_NUMERICAL_EXPRESSION"
]

t_SEPARATOR = r"(\s)"
t_PUNCTUATION_MARK = r"[\.,!?:;]"
t_DIGIT = r"\d"
t_CHAR = r"[A-Z]"
t_NUMBER = f"(-?{t_DIGIT}+.?{t_DIGIT}*)"
t_SYMBOL = f"({t_DIGIT}|{t_CHAR}|{t_PUNCTUATION_MARK}|{t_SEPARATOR})"
t_STRING = f"\"{t_SYMBOL}*\""
t_ID = f"({t_CHAR}|_)({t_CHAR}|_|{t_DIGIT})*" 
t_NUMERICAL_OPERATOR = r"[+\-*/]"
# t_NUMERICAL_EXPRESSION = r"(?1)|\((?1)\)"
# t_NUMERICAL_FACTOR = f"({t_NUMBER}|{t_NUMBER} {t_NUMERICAL_OPERATOR} {t_NUMERICAL_EXPRESSION}"

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


def t_error(t):
    print(f"Illegal character '{t.value[0]}' on line {t.lineno} column {t.lexpos}")
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex(debug=True)

if __name__ == "__main__":
    lex.runmain()
