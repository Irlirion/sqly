import ply.lex as lex
from ply.lex import TOKEN

from utils import find_column, find_line, runmain_upper


class SelectLexer(object):
    """Lexer object for parse SELECT expression"""

    literals = "()+-*/;"

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
        "NUMBER",
        "STRING",
        "ID",
        "COMPARSION_OPERATOR",
        "CONDITIONAL_OPERATOR",
    ]

    tokens += reserved.values()

    punctuation_mark = r"[.,!?:;]"
    separator = r"(\s)"
    digit = r"(\d)"
    char = r"[A-Z]"
    symbol = f"({digit}|{char}|{punctuation_mark}|{separator})"
    t_STRING = f'"{symbol}*"'
    t_COMPARSION_OPERATOR = r"(<>|<=|>=|<|>|=)"

    t_ignore = " \t"

    identifier = f"({char}|_)({char}|_|{digit})*"
    number = f"(-?{digit}+\.?{digit}*)"
        
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
    select_lexer.build(debug=True)
    runmain_upper(lexer=select_lexer.lexer)
