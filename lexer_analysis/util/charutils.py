def isLetter(char):
    return char.isalpha()


def isDigit(char):
    return char.isdigit()


def isLetterOrDigit(char):
    return char.isalnum()


def isWhitespace(char):
    return char == ' '


def isDelimiter(char):
    return char == '(' or char == ')' or char == ',' or char == ';' or char == '.'


def isNewLine(char):
    return char == '\n'


def isComparisonOperator(char):
    return char == '=' or char == '>' or char == '<' or char == ':' or char == '#'


def isArithmeticOperator(char):
    return char == '+' or char == '-' or char == '*' or char == '/'
