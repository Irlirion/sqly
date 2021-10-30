import ply.lex as lex
from ply.lex import TOKEN

from utils import find_column, find_line, runmain_upper


class SelectLexer(object):
    """Lexer object for parse SELECT expression"""

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
    t_PUNCTUATION_MARK = r"[.,!?:;]"
    t_DIGIT = r"(\d)"
    t_CHAR = r"[A-Z]"
    t_SYMBOL = f"({t_DIGIT}|{t_CHAR}|{t_PUNCTUATION_MARK}|{t_SEPARATOR})"
    t_STRING = f'"{t_SYMBOL}*"'
    t_NUMERICAL_OPERATOR = r"[+\-*/]"
    t_COMPARSION_OPERATOR = r"(<>|<=|>=|<|>|=)"

    identifier = f"({t_CHAR}|_)({t_CHAR}|_|{t_DIGIT})*"
    number = f"(-?{t_DIGIT}+\.?{t_DIGIT}*)"

    @TOKEN(number)
    def t_NUMBER(self, t):
        return t

    def t_CONDITIONAL_OPERATOR(self, t):
        r"(AND|OR)"
        return t

    @TOKEN(identifier)
    def t_ID(self, t):
        t.type = self.reserved.get(t.value, "ID")
        return t

    def t_newline(self, t):
        r"\n+"
        t.lexer.lineno += len(t.value)

    def t_error(self, t):
        raise SyntaxError(
            f"illegal character '{t.value[0]}'",
            (
                None,
                t.lineno,
                find_column(t.lexer.lexdata, t.lexpos),
                t.lexer.lexdata[find_line(t.lexer.lexdata, t.lexpos)],
            ),
        )

    def build(self, **kwargs):
        """Build the lexer"""

        self.lexer = lex.lex(module=self, **kwargs)


if __name__ == "__main__":
    select_lexer = SelectLexer()
    select_lexer.build(optimize=True)
    runmain_upper(lexer=select_lexer.lexer)
