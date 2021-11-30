import sys


def find_column(input, pos: int):
    line_start = input.rfind("\n", 0, pos) + 1
    return (pos - line_start) + 1


def find_line(input: str, pos: int):
    line_start = input.rfind("\n", 0, pos) + 1
    line_end = input.find("\n", line_start)
    return slice(line_start, line_end)


def raise_error(t):
    print('-'*80)
    print(t.lexer.lexdata[find_line(t.lexer.lexdata, t.lexpos)])
    column = find_column(t.lexer.lexdata, t.lexpos) - 2
    print(' ' * column, '^')
    print(f"SyntaxError on line {t.lineno+1}: illegal character '{t.value[0]}'")
    print('-'*80)

def runmain_upper(lexer=None, data=None):
    if not data:
        try:
            filename = sys.argv[1]
            f = open(filename)
            data = f.read().upper()
            f.close()
        except IndexError:
            sys.stdout.write("Reading from standard input (type EOF to end):\n")
            data = sys.stdin.read()

    if lexer:
        _input = lexer.input
    else:
        _input = input
    _input(data)
    if lexer:
        _token = lexer.token
    else:
        _token = token  # type: ignore

    while True:
        tok = _token()
        if not tok:
            break
        sys.stdout.write(
            "(%s,%r,%d,%d)\n" % (tok.type, tok.value, tok.lineno, tok.lexpos)
        )
