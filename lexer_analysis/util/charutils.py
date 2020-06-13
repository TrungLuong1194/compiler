def isLetter(char):
    return char.isalpha()


def isDigit(char):
    return char.isdigit()


def isLetterOrDigit(char):
    return char.isalnum()


def isWhitespace(char):
    return char == ' '


def isDelimiter(char):
    return char == '{' or char == '[' or char == '(' or char == '}' or \
           char == ']' or char == ')' or char == ':' or char == ','


def isNewLine(char):
    return char == '\n'


def isDot(char):
    return char == '.'


def isOperator(char):
    return char == '+' or char == '-' or char == '*' or char == '/' or \
           char == '=' or char == '>' or char == '<' or char == '!' or \
           char == '&' or char == '|' or char == '%' or char == '~' or \
           char == '$' or char == '~' or char == '^'


def isComparisonOperator(char):
    return char == '=' or char == '>' or char == '<' or char == '!'


def isArithmeticOperator(char):
    return char == '+' or char == '-' or char == '*' or char == '/'


def isIdentifierPart(char):
    return char == '_' or isLetterOrDigit(char) or isOperator(char)


def isBeginningOfIdentifier(char):
    return isLetter(char) or char == '_'


def isBeginningOfNumber(char):
    return isDigit(char) or char == '.'


def isBeginningOfString(char):
    return char == '"'


def isExponentSymbol(char):
    return char == 'e' or char == 'E'


def isBeginningOfLiteral(char):
    return isLetter(char) or isBeginningOfIdentifier(char) or \
           isBeginningOfNumber(char) or isBeginningOfString(char)


def isEscapeCharacter(char):
    return char == '\\'


def isEndOfEscapeSequence(char):
    return char == '\"' or char == '\\' or char == 'n' or \
           char == 'r' or char == 't' or char == 'b' or \
           char == 'f' or char == 'v' or char == '0'


def isStringDelimiter(char):
    return char == '\"'
