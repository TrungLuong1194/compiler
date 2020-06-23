from lexer_analysis.token.tokentype import TokenType
import syntax_analysis_ast.ast.ast as ast


class Parser:
    """
    Recursive-descent parser
    """

    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0
        self.current_token = self.tokens[self.index]

    def matching(self):
        self.index += 1
        self.current_token = self.tokens[self.index]

    def identifier(self):
        token = self.current_token

        if token.typeToken == TokenType.Identifier.name:
            self.matching()
            return ast.Identifier(token)
        else:
            raise Exception("Identifier don't matching - " + str(token.value) + ' - ' + str(token.line))

    def factor(self):
        """
        factor = ident | number | "(" expression ")"
        """
        token = self.current_token

        if token.typeToken == TokenType.Identifier.name:
            self.matching()
            return ast.Identifier(token)
        elif token.typeToken == TokenType.Number.name:
            self.matching()
            return ast.Number(token)
        elif token.typeToken == TokenType.LeftParen.name:
            self.matching()
            node = self.expression()
            if self.current_token.typeToken == TokenType.RightParen.name:
                self.matching()
            else:
                raise Exception("Factor: ')' don't matching")

            return node
        else:
            raise Exception("Factor don't matching - " + str(token.value) + ' - ' + str(token.line))

    def term(self):
        """
        term = factor { ( "*"|"/" ) factor }
        """
        node = self.factor()

        while self.current_token.typeToken in (TokenType.Mul.name, TokenType.Div.name):
            token = self.current_token
            if token.typeToken == TokenType.Mul.name:
                self.matching()
            elif token.typeToken == TokenType.Div.name:
                self.matching()

            node = ast.BinOp(node, token, self.factor())

        return node

    def expression(self):
        """
        expression = [ "+"|"-" ] term { ( "+"|"-" ) term }
        """
        token = self.current_token

        if token.typeToken == TokenType.Plus.name:
            self.matching()
            node = ast.UnaryOp(token, self.term())
        elif token.typeToken == TokenType.Minus.name:
            self.matching()
            node = ast.UnaryOp(token, self.term())
        else:
            node = self.term()

        while self.current_token.typeToken in (TokenType.Plus.name, TokenType.Minus.name):
            token = self.current_token
            if token.typeToken == TokenType.Plus.name:
                self.matching()
            elif token.typeToken == TokenType.Minus.name:
                self.matching()

            node = ast.BinOp(node, token, self.term())

        return node

    def condition(self):
        """
        condition = "odd" expression | expression ( "="|"#"|"<"|"<="|">"|">=" ) expression
        """
        token = self.current_token

        if token.typeToken == TokenType.Odd.value:
            self.matching()
            node = self.expression()
        else:
            node = self.expression()

            token = self.current_token

            if token.typeToken == TokenType.Greater.name:
                self.matching()
            elif token.typeToken == TokenType.GreaterOrEqual.name:
                self.matching()
            elif token.typeToken == TokenType.Less.name:
                self.matching()
            elif token.typeToken == TokenType.LessOrEqual.name:
                self.matching()
            elif token.typeToken == TokenType.NotEqual.name:
                self.matching()
            elif token.typeToken == TokenType.Equal.name:
                self.matching()
            else:
                raise Exception("Condition: Relational operator don't matching - " + str(token.value) + ' - ' +
                                str(token.line))

            node = ast.RelOp(node, token, self.expression())

        return node

    def statement(self):
        """
        statement = [ ident ":=" expression
                    | "call" ident
                    | "read" ident
                    | "write" expression
                    | "begin" statement { ";" statement } "end"
                    | "if" condition "then" statement
                    | "while" condition "do" statement ]
        """
        token = self.current_token

        if token.typeToken == TokenType.Identifier.name:
            self.matching()
            node = ast.Identifier(token)

            token = self.current_token
            if token.typeToken == TokenType.Assign.name:
                self.matching()
            else:
                raise Exception("Statement: ':=' don't matching - " + str(token.value) + ' - ' + str(token.line))

            node = ast.Assign(node, self.expression())

        elif token.typeToken == TokenType.Call.value:
            self.matching()
            token = self.current_token

            if token.typeToken == TokenType.Identifier.name:
                self.matching()

                node = ast.Identifier(token)
            else:
                raise Exception("Statement: Call: Identifier don't matching - " + str(token.value) + ' - ' +
                                str(token.line))

            node = ast.Call(node)

        elif token.typeToken == TokenType.Read.value:
            self.matching()
            token = self.current_token

            if token.typeToken == TokenType.Identifier.name:
                self.matching()

                node = ast.Identifier(token)
            else:
                raise Exception("Statement: Read: Identifier don't matching - " + str(token.value) + ' - ' +
                                str(token.line))

            node = ast.Read(node)

        elif token.typeToken == TokenType.Write.value:
            self.matching()

            node = ast.Write(self.expression())

        elif token.typeToken == TokenType.Begin.value:
            self.matching()
            statement_list = [self.statement()]

            while self.current_token.typeToken == TokenType.SemiColon.name:
                self.matching()
                statement_list.append(self.statement())

            if self.current_token.typeToken == TokenType.End.value:
                self.matching()
            else:
                raise Exception("Statement: 'end' don't matching" + ' - ' + str(token.line))

            node = ast.BeginEnd(statement_list)

        elif token.typeToken == TokenType.If.value:
            self.matching()
            condition = self.condition()

            if self.current_token.typeToken == TokenType.Then.value:
                self.matching()

                statement = self.statement()
            else:
                raise Exception("Statement: 'then' don't matching" + ' - ' + str(token.line))

            node = ast.If(condition, statement)

        elif token.typeToken == TokenType.While.value:
            self.matching()
            condition = self.condition()

            if self.current_token.typeToken == TokenType.Do.value:
                self.matching()

                statement = self.statement()
            else:
                raise Exception("Statement: 'do' don't matching" + ' - ' + str(token.line))

            node = ast.While(condition, statement)

        else:
            node = ast.NoOp()

        return node

    def var_declaration(self):
        """
        var_declaration = "var" ident { "," ident } ";"
        """
        ident_list = []

        token = self.current_token
        if token.typeToken == TokenType.Var.value:
            self.matching()

            token = self.current_token
            if token.typeToken == TokenType.Identifier.name:
                self.matching()

                node = ast.Identifier(token)
            else:
                raise Exception("Var declaration: Identifier don't matching " + str(token.value) + ' - ' +
                                str(token.line))

            ident_list.append(node)

            while self.current_token.typeToken == TokenType.Colon.name:
                self.matching()

                token = self.current_token
                if token.typeToken == TokenType.Identifier.name:
                    self.matching()

                    node = ast.Identifier(token)
                else:
                    raise Exception("Var declaration: Nested: Identifier don't matching " + str(token.value) + ' - ' +
                                    str(token.line))

                ident_list.append(node)

            if self.current_token.typeToken == TokenType.SemiColon.name:
                self.matching()
            else:
                raise Exception("Var declaration: ';' don't matching " + str(self.current_token.value) + ' - ' +
                                str(token.line))

            node = ast.VarDec(ident_list)

        else:
            raise Exception("Var declaration: 'var' don't matching" + ' - ' + str(token.line))

        return node

    def procedure_declaration(self):
        """
        procedure_declaration = "procedure" ident ";" block ";"
        """
        token = self.current_token

        if token.typeToken == TokenType.Procedure.value:
            self.matching()

            token = self.current_token
            if token.typeToken == TokenType.Identifier.name:
                self.matching()
                identifier = ast.Identifier(token)
            else:
                raise Exception("Procedure declaration: Identifier don't matching " + str(token.value) + ' - ' +
                                str(token.line))

            if self.current_token.typeToken == TokenType.SemiColon.name:
                self.matching()
            else:
                raise Exception("Procedure declaration: ';' first don't matching" + ' - ' + str(token.line))

            block = self.block()

            if self.current_token.typeToken == TokenType.SemiColon.name:
                self.matching()
            else:
                raise Exception("Procedure declaration: ';' second don't matching" + ' - ' + str(token.line))

            node = ast.Procedure(identifier, block)

        else:
            raise Exception("Procedure declaration: 'procedure' don't matching" + ' - ' + str(token.line))

        return node

    def block(self):
        """
        block = [ var_declaration ] { procedure_declaration } statement
        """
        var_declaration = ast.NoOp()

        if self.current_token.typeToken == TokenType.Var.value:
            var_declaration = self.var_declaration()

        procedure_declaration = ast.NoOp()

        while self.current_token.typeToken == TokenType.Procedure.value:
            procedure_declaration = self.procedure_declaration()

        statement = self.statement()

        return ast.Block(var_declaration, procedure_declaration, statement)

    def program(self):
        """
        program = block "."
        """
        block = self.block()

        if self.current_token.typeToken == TokenType.Dot.name:
            self.matching()
        else:
            raise Exception("Program: '.' don't matching" + ' - ' + str(self.current_token.line))

        return ast.Program(block)

    def parse(self):
        node = self.program()

        if self.current_token.typeToken != TokenType.EndOfInput.name:
            raise Exception("End of input don't matching" + ' - ' + str(self.current_token.line))
        else:
            print('Build abstract syntax tree successfully!')

        return node
