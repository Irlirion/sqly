# ------------------------------------------------------------
# lex_select.py
#
# tokenizer for a SQL SELECT expression evaluator
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required
tokens = (
    "TABLE_NAME",
    "CONDITION",
    "FIELD_LIST",
    "FIELD_NAME",
    "CONDITION_FACTOR",
    "PREDICATE",
    "CONDITIONAL_OPERATOR",
    "FIELD_VALUE",
    "COMPARSION_OPERATOR",
    "VALUE",
    "STRING",
    "NUMERIC_EPRESSION",
    "NUMERICAL_FACTOR",
    "NUMBER",
    "NUMERICAL_OPERATOR",
    "PUNCTUATION_MARK",
    "INTEGER",
    "SELECT",
    "DISTINCT_ALL",
    "ID",
    "NULL",
    "DEFAULT",
    "DISTINCT",
    "ALL",
)

t_NUMERICAL_OPERATOR = r"[+\-*/]"
t_COMPARSION_OPERATOR = r"<>|<=|>=|<|>|="
t_PUNCTUATION_MARK = r"[\.,!?:;]"
t_ID = r"[A-Z_][A-Z_\d]*"


def t_SELECT(t):
    r"SELECT"
    return t


def t_DISTINCT_ALL(t):
    r"DISTINCT|ALL"
    return t


def t_NULL(t):
    r"NULL"
    return t


def t_DEFAULT(t):
    r"DEFAULT"
    return t


def t_CONDITIONAL_OPERATOR(t):
    r"AND|OR"
    return t


def t_INTEGER(t):
    r"[-+]?\d+"
    t.value = int(t.value)
    return t


def t_STRING(t):
    r'"[A-Z\d.,!?:;\s]+"'
    t.type = "STRING"
    return t


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


t_ignore = r" \t"


def t_error(t):
    print(f"Illegal character '{t.value[0]}' on line {t.lineno}")
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex(debug=True)

if __name__ == "__main__":
    lex.runmain()
