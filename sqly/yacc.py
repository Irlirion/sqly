import sys
import ply.yacc as yacc
from sqly.lex import SelectLexer
from utils import find_column, find_line, raise_error

selectlexer = SelectLexer()
selectlexer.build()
tokens = selectlexer.tokens

def p_select_list(p):
    """select_list : select
                   | select select_list"""
def p_select(p):
    """select : select_part from_part where_part ';'
              | select_part from_part ';'"""

def p_select_part(p):
    """select_part : SELECT select_opt field_list
                   | SELECT field_list"""

def p_select_part_error(p):
     'select_part : SELECT error'

def p_select_opt(p):
    """select_opt : DISTINCT
                  | ALL"""

def p_field_list(p):
    """field_list : '*'
                  | field_name ',' field_list
                  | field_name"""

def p_field_name(p):
    """field_name : ID"""

def p_from_part(p):
    """from_part : FROM tabel_list"""

def p_from_part_error(p):
     """from_part : FROM error"""

def p_tabel_list(p):
    """tabel_list : tabel_name ',' tabel_list
                  | tabel_name"""

def p_tabel_name(p):
    """tabel_name : ID"""

def p_where_part(p):
    """where_part : WHERE condition"""

def p_where_part_error(p):
    """where_part : WHERE error"""

def p_confition(p):
    """condition : predicate
                 | '(' condition ')'
                 | condition AND condition
                 | condition OR condition"""

def p_predicate(p):
    """predicate : field_value COMPARSION_OPERATOR field_value
                 | NOT predicate"""

def p_field_value(p):
    """field_value : value
                   | field_name"""

def p_value(p):
    """value : STRING
             | numeric_expression
             | NULL
             | DEFAULT"""

def p_numeric_expression(p):
    """numeric_expression : NUMBER
                      | '(' numeric_expression ')'
                      | numeric_expression '+' numeric_expression
                      | numeric_expression '-' numeric_expression
                      | numeric_expression '*' numeric_expression
                      | numeric_expression '/' numeric_expression"""


precedence = (
    ('left', '+', '-', 'OR'),
    ('left', '*', '/', 'AND'),
)

def p_error(t):
    raise_error(t)


# Build the grammar
def make_parser(debug=False):
    return yacc.yacc(debug=debug)

def main():
    import argparse
    import os

    ap = argparse.ArgumentParser(description="Parser test tool")
    ap.add_argument('-g', '--generate', dest='generate', action='store_true')
    ap.add_argument('-r', '--recursive', dest='recursive', action='store_true')
    ap.add_argument('-d', '--debug', dest='debug', action='store_true')
    ap.add_argument('path', metavar='PATH', nargs='?', type=str)
    args = ap.parse_args()

    if args.generate:
        make_parser(args.debug)
        return

    parser = make_parser(args.debug)
    if args.path is None:
        run_parser(parser, sys.stdin, args.debug)
    elif os.path.isfile(args.path):
        with open(args.path, 'r') as f:
            run_parser(parser, f, args.debug)
    elif os.path.isdir(args.path):
        if not args.recursive:
            print('directory path given, use -r for recursive processing')
        else:
            for root, _, files in os.walk(args.path):
                for fpath in files:
                    if not fpath.endswith('.php'):
                        continue
                    with open(os.path.join(root, fpath), 'r') as f:
                        run_parser(parser, f, args.debug)

def run_parser(parser, source, debug):
    s = source.read()

    lexer = selectlexer.lexer
    lexer.lineno = 1

    parser.parse(s, lexer=lexer.clone(), debug=debug)


if __name__ == '__main__':
    main()