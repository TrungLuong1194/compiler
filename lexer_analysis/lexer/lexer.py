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

        if util.isDigit(character):
            return self.recognizeNumber()

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

                if util.isLetter(self.input[self.position + offset]):
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

        token.initValue(value, value, self.line, self.column + 1)

        return token

    def recognizeIdentifier(self):
        token = Token()

        fsm = self.buildIdentifierRecognizer()
        recognized, ID = fsm.run(self.input[self.position:])

        column = self.column + 1

        if not recognized:
            raise Exception(str(self.line) + ':' + str(column) + ' - ' + 'Unrecognized identifier literal.')

        self.position += len(ID)
        self.column += len(ID)

        token.initValue(TokenType.Identifier.name, ID, self.line, column)

        return token

    def buildIdentifierRecognizer(self):
        """
        letter     = [a-Z]
        ID         = letter letter*
        """
        fsm = FSM()

        fsm.states = [State.InitialID.value, State.FinalID.value]

        fsm.initialState = State.InitialID.value

        fsm.acceptingStates = [State.FinalID.value]

        fsm.nextState = lambda currentState, character: \
            State.FinalID.value if (currentState == State.InitialID.value and util.isLetter(character)) else \
                State.FinalID.value if (currentState == State.FinalID.value and util.isLetter(character)) else \
                    State.NoNextState.value

        return fsm

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
        number     = digit digit*
        """
        fsm = FSM()

        fsm.states = [State.InitialNumber.value, State.FinalNumber.value]

        fsm.initialState = State.InitialNumber.value

        fsm.acceptingStates = [State.FinalNumber.value]

        fsm.nextState = lambda currentState, character: \
            State.FinalNumber.value if (currentState == State.InitialNumber.value and util.isDigit(character)) else \
                State.FinalNumber.value if (currentState == State.FinalNumber.value and util.isDigit(character)) else \
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
            token.initValue(TokenType.Colon.name, TokenType.Colon.value, self.line, self.column)
            return token
        elif character == ';':
            token.initValue(TokenType.SemiColon.name, TokenType.SemiColon.value, self.line, self.column)
            return token
        else:
            raise Exception(
                str(self.line) + ':' + str(self.column) + ' - ' + 'Unrecognized token ' + str(character))

    def skipWhitespaces(self):
        while self.position < len(self.input) and util.isWhitespace(self.input[self.position]):
            self.position += 1
            self.column += 1
