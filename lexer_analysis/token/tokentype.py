from enum import Enum


class TokenType(Enum):
    # Keywords
    Const = 'const'
    Var = 'var'
    Procedure = 'procedure'
    Call = 'call'
    Begin = 'begin'
    End = 'end'
    If = 'if'
    Then = 'then'
    While = 'while'
    Do = 'do'
    Odd = 'odd'
    Write = 'write'
    Read = 'read'

    # Literals
    Identifier = 'identifier'
    Number = 'number'

    # Delimiters
    Colon = ','
    SemiColon = ';'
    Dot = '.'
    LeftParen = '('
    RightParen = ')'

    # Comparison operators
    Greater = '>'
    GreaterOrEqual = '>='
    Less = '<'
    LessOrEqual = '<='
    NotEqual = '#'
    Equal = '='
    Assign = ':='

    # Arithmetic operators
    Plus = '+'
    Minus = '-'
    Mul = '*'
    Div = '/'

    # Special tokens
    EndOfInput = 'EndOfInput'
    Newline = 'NewLine'
