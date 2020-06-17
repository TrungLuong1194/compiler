from enum import Enum


class TokenType(Enum):
    # Keywords
    AS = 'as'
    CLASS = 'class'
    ELSE = 'else'
    FALSE = 'False'
    DEF = 'def'
    FOR = 'for'
    IF = 'if'
    IN = 'in'
    RETURN = 'return'
    SELF = 'self'
    TRUE = 'True'
    WHILE = 'while'
    PRINT = 'print'
    RANGE = 'range'
    LEN = 'len'
    NONE = 'None'

    # Assignment operators
    DivEqual = '/='
    Equal = '='
    MinusEqual = '-='
    PlusEqual = '+='
    MulEqual = '*='

    # Arithmetic operators
    Plus = '+'
    Minus = '-'
    Mul = '*'
    Div = '/'

    # Comparison operators
    DoubleEqual = '=='
    Greater = '>'
    GreaterOrEqual = '>='
    Less = '<'
    LessOrEqual = '<='
    NotEqual = '!='

    # Boolean operators
    And = 'and'
    Not = 'not'
    Or = 'or'

    # Literals
    Identifier = 'IDENTIFIER'
    String = 'STRING'
    Number = 'NUMBER'
    Keyword = 'KEYWORD'

    # Delimiters
    Colon = ':'
    Comma = ','
    LeftBrace = '{'
    LeftBracket = '['
    LeftParen = '('
    Newline = 'NewLine'
    Tab = 'Tab'
    RightBrace = '}'
    RightBracket = ']'
    RightParen = ')'

    # Special tokens
    EndOfInput = 'EndOfInput'
