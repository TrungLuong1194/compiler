from enum import Enum


class TokenType(Enum):
    # Keywords
    ELSE = 'else'
    IF = 'if'
    INT = 'int'
    RETURN = 'return'
    VOID = 'void'
    WHILE = 'while'

    # Literals
    Identifier = 'ID'
    Number = 'NUMBER'
    Keyword = 'KEYWORD'
    Delimiter = 'DELIMITER'
    Operator = 'OPERATOR'

    # Delimiters
    Colon = ','
    SemiColon = ';'
    LeftBrace = '{'
    LeftBracket = '['
    LeftParen = '('
    RightBrace = '}'
    RightBracket = ']'
    RightParen = ')'

    # Comparison operators
    DoubleEqual = '=='
    Greater = '>'
    GreaterOrEqual = '>='
    Less = '<'
    LessOrEqual = '<='
    NotEqual = '!='
    Equal = '='

    # Arithmetic operators
    Plus = '+'
    Minus = '-'
    Mul = '*'
    Div = '/'

    # Special tokens
    EndOfInput = 'EndOfInput'
    Newline = 'NewLine'
