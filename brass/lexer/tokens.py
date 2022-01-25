from string import ascii_letters

# Constants
DIGITS = '0123456789'

NAME_CHARS_START = ascii_letters + '_'
NAME_CHARS = NAME_CHARS_START + DIGITS

# Operators
operators = {'+', '-', '*', '/', '^', '%', '=', '&', '|'}

TT_PLUS = '+'
TT_MINUS = '-'
TT_MUL = '*'
TT_DIV = '/'
TT_POW = '^'
TT_MOD = '%'
TT_EQ = '='
TT_AND = '&'
TT_PIPE = '|'

# Seperators
seperators = {'(', ')', '{', '}', '[', ']', '<', '>', ',', '.', ':', ';'}

TT_LPAREN = '('
TT_RPAREN = ')'
TT_LBRACE = '{'
TT_RBRACE = '}'
TT_LBRACKET = '['
TT_RBRACKET = ']'
TT_LCHEV = '<'
TT_RCHEV = '>'
TT_COMMA = ','
TT_DOT = '.'
TT_COLON = ':'
TT_SCOLON = ';'


NAMES = {
    TT_PLUS: 'TT_PLUS',
    TT_MINUS: 'TT_MINUS',
    TT_MUL: 'TT_MUL',
    TT_DIV: 'TT_DIV',
    TT_POW: 'TT_POW',
    TT_MOD: 'TT_MOD',
    TT_EQ: 'TT_EQ',
    TT_AND: 'TT_AND',
    TT_PIPE: 'TT_PIPE',
    TT_LPAREN: 'TT_LPAREN',
    TT_RPAREN: 'TT_RPAREN',
    TT_LBRACE: 'TT_LBRACE',
    TT_RBRACE: 'TT_RBRACE',
    TT_LBRACKET: 'TT_LBRACKET',
    TT_RBRACKET: 'TT_RBRACKET',
    TT_LCHEV: 'TT_LCHEV',
    TT_RCHEV: 'TT_RCHEV',
    TT_COMMA: 'TT_COMMA',
    TT_DOT: 'TT_DOT',
    TT_COLON: 'TT_COLON',
    TT_SCOLON: 'TT_SCOLON'
}