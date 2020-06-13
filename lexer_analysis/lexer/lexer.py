from lexer_analysis.token.tokentype import TokenType
from lexer_analysis.token.token import Token
from lexer_analysis.fsm.fsm import FSM
from lexer_analysis.util.state import State
import lexer_analysis.util.charutils as util


class Lexer:
    def __init__(self, input):
        self.input = input
        self.position = 0
        self.line = 1
        self.column = 0

    def tokenize(self):
        tokens = []
        token = Token()

        while token.typeToken != TokenType.EndOfInput.value:
            token = self.nextToken()

            tokens.append(token)

        return tokens

    def nextToken(self):
        self.skipWhitespaces()

        if self.position >= len(self.input):
            token = Token()
            token.initValue(TokenType.EndOfInput.value, None, None, None)
            return token

        character = self.input[self.position]

        if util.isLetter(character):
            return self.recognizeKeywordOrIdentifier()

        if util.isBeginningOfIdentifier(character):
            return self.recognizeIdentifier()

        if util.isBeginningOfNumber(character):
            return self.recognizeNumber()

        if util.isBeginningOfString(character):
            return self.recognizeString()

        if util.isComparisonOperator(character):
            return self.recognizeComparisonOperator()

        if util.isArithmeticOperator(character):
            return self.recognizeArithmeticOperator()

        if util.isDelimiter(character):
            return self.recognizeDelimiter()

        if util.isNewLine(character):
            self.position += 1
            self.line += 1
            self.column = 0

            token = Token()
            token.initValue(TokenType.Newline.value, None, None, None)

            return token

        raise Exception(str(self.line) + ':' + str(self.column) + ' - ' + 'Unrecognized token ' + str(character))

    def recognizeKeywordOrIdentifier(self):
        token = self.recognizeKeyword()

        if token:
            return token
        else:
            return self.recognizeIdentifier()

    def recognizeKeyword(self):
        character = self.input[self.position]

        keywords = []

        for ele in TokenType:
            if ele.value[0] == character:
                keywords.append(ele.value)

        for value in keywords:
            token = self.recognizeToken(value)

            if token:
                offset = len(token.value)

                if util.isIdentifierPart(self.input[self.position + offset]):
                    return None

                self.position += offset
                self.column += offset

                return token

        return None

    def recognizeToken(self, value):
        token = Token()

        for i in range(len(value)):
            if self.input[self.position + i] != value[i]:
                return None

        token.initValue(TokenType.Keyword.name, value, self.line, self.column + 1)

        return token

    def recognizeIdentifier(self):
        token = Token()
        identifier = ''

        column = self.column + 1

        while self.position < len(self.input):
            character = self.input[self.position]

            if not util.isIdentifierPart(character):
                break

            identifier += character
            self.position += 1
            self.column += 1

        token.initValue(TokenType.Identifier.value, identifier, self.line, column)

        return token

    def recognizeNumber(self):
        token = Token()

        fsm = self.buildNumberRecognizer()
        recognized, number = fsm.run(self.input[self.position:])

        column = self.column + 1

        if not recognized:
            raise Exception(str(self.line) + ':' + str(column) + ' - ' + 'Unrecognized number literal.')

        self.position += len(number)
        self.column += len(number)

        token.initValue(TokenType.Number.name, number, self.line, column)

        return token

    def buildNumberRecognizer(self):
        """
        digit      = [0-9]
        digits     = digit digit*
        fraction   = .digits | eps
        number     = digits fraction
        """
        fsm = FSM()

        fsm.states = [State.Initial.value, State.Integer.value, State.BeginNumberWithFractionPart.value,
                      State.NumberWithFractionPart.value]

        fsm.initialState = State.Initial.value

        fsm.acceptingStates = [State.Integer.value, State.NumberWithFractionPart.value]

        fsm.nextState = lambda currentState, character: \
            State.Integer.value if (currentState == State.Initial.value and util.isDigit(character)) else \
                State.Integer.value if (currentState == State.Integer.value and util.isDigit(character)) else \
                    State.BeginNumberWithFractionPart.value if (
                            currentState == State.Integer.value and character == '.') else \
                        State.NumberWithFractionPart.value if (
                                currentState == State.BeginNumberWithFractionPart.value and util.isDigit(
                            character)) else \
                            State.NumberWithFractionPart.value if (
                                    currentState == State.NumberWithFractionPart.value and util.isDigit(character)) else \
                                State.NoNextState.value

        return fsm

    def recognizeString(self):
        token = Token()

        fsm = self.buildStringRecognizer()
        recognized, string = fsm.run(self.input[self.position:])

        column = self.column + 1

        if not recognized:
            raise Exception('Line ' + str(self.line) + ' - ' + 'Invalid string literal.')

        self.position += len(string)
        self.column += len(string)

        token.initValue(TokenType.String.name, string, self.line, column)

        return token

    def buildStringRecognizer(self):
        """
        id      = digit | letter | '_' | operator
        string  = "id*"
        """
        fsm = FSM()

        fsm.states = [State.Initial.value, State.OpenString.value, State.String.value]

        fsm.initialState = State.Initial.value

        fsm.acceptingStates = [State.String.value]

        fsm.nextState = lambda currentState, character: \
            State.OpenString.value if (currentState == State.Initial.value and character == '"') else \
                State.OpenString.value if (
                        currentState == State.OpenString.value and util.isIdentifierPart(character)) else \
                    State.String.value if (currentState == State.OpenString.value and character == '"') else \
                        State.NoNextState.value

        return fsm

    def recognizeComparisonOperator(self):
        token = Token()
        character = self.input[self.position]

        if self.position + 1 < len(self.input):
            lookahead = self.input[self.position + 1]
        else:
            lookahead = None

        isLookaheadEqualSymbol = lookahead is not None and lookahead == '='

        self.position += 1
        self.column += 1
        column = self.column

        if isLookaheadEqualSymbol:
            self.position += 1
            self.column += 1

        if character == '>':
            if isLookaheadEqualSymbol:
                token.initValue(TokenType.GreaterOrEqual.name, TokenType.GreaterOrEqual.value, self.line, column)
                return token
            else:
                token.initValue(TokenType.Greater.name, TokenType.Greater.value, self.line, column)
                return token
        elif character == '<':
            if isLookaheadEqualSymbol:
                token.initValue(TokenType.LessOrEqual.name, TokenType.LessOrEqual.value, self.line, column)
                return token
            else:
                token.initValue(TokenType.Less.name, TokenType.Less.value, self.line, column)
                return token
        elif character == '=':
            if isLookaheadEqualSymbol:
                token.initValue(TokenType.DoubleEqual.name, TokenType.DoubleEqual.value, self.line, column)
                return token
            else:
                token.initValue(TokenType.Equal.name, TokenType.Equal.value, self.line, column)
                return token
        elif character == '!':
            if isLookaheadEqualSymbol:
                token.initValue(TokenType.NotEqual.name, TokenType.NotEqual.value, self.line, column)
                return token
            else:
                raise Exception(
                    str(self.line) + ':' + str(column) + ' - ' + 'Unrecognized token ' + str(character))
        else:
            raise Exception(
                str(self.line) + ':' + str(column) + ' - ' + 'Unrecognized token ' + str(character))

    def recognizeArithmeticOperator(self):
        token = Token()
        character = self.input[self.position]

        self.position += 1
        self.column += 1

        if character == '+':
            token.initValue(TokenType.Plus.name, TokenType.Plus.value, self.line, self.column)
            return token
        elif character == '-':
            token.initValue(TokenType.Minus.name, TokenType.Minus.value, self.line, self.column)
            return token
        elif character == '*':
            token.initValue(TokenType.Mul.name, TokenType.Mul.value, self.line, self.column)
            return token
        elif character == '/':
            token.initValue(TokenType.Div.name, TokenType.Div.value, self.line, self.column)
            return token
        else:
            raise Exception(
                str(self.line) + ':' + str(self.column) + ' - ' + 'Unrecognized token ' + str(character))

    def recognizeDelimiter(self):
        token = Token()
        character = self.input[self.position]

        self.position += 1
        self.column += 1

        if character == '{':
            token.initValue(TokenType.LeftBrace.name, TokenType.LeftBrace.value, self.line, self.column)
            return token
        elif character == '}':
            token.initValue(TokenType.RightBrace.name, TokenType.RightBrace.value, self.line, self.column)
            return token
        elif character == '[':
            token.initValue(TokenType.LeftBracket.name, TokenType.LeftBracket.value, self.line, self.column)
            return token
        elif character == ']':
            token.initValue(TokenType.RightBracket.name, TokenType.RightBracket.value, self.line, self.column)
            return token
        elif character == '(':
            token.initValue(TokenType.LeftParen.name, TokenType.LeftParen.value, self.line, self.column)
            return token
        elif character == ')':
            token.initValue(TokenType.RightParen.name, TokenType.RightParen.value, self.line, self.column)
            return token
        elif character == ',':
            token.initValue(TokenType.Comma.name, TokenType.Comma.value, self.line, self.column)
            return token
        elif character == ':':
            token.initValue(TokenType.Colon.name, TokenType.Colon.value, self.line, self.column)
            return token
        else:
            raise Exception(
                str(self.line) + ':' + str(self.column) + ' - ' + 'Unrecognized token ' + str(character))

    def skipWhitespaces(self):
        while self.position < len(self.input) and util.isWhitespace(self.input[self.position]):
            self.position += 1
            self.column += 1
