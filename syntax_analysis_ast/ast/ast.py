class AST:
    pass


class Number(AST):
    """
    Represent a number
    """

    def __init__(self, token):
        self.token = token
        self.value = int(token.value)


class Identifier(AST):
    """
    Represent an identifier
    """

    def __init__(self, token):
        self.token = token
        self.value = token.value


class BinOp(AST):
    """
    Represent a binary operator
    Ex: 4 * 5; 6 - 3
    """

    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right


class UnaryOp(AST):
    """
    Represent a unary operator
    Ex: -5; +7
    """

    def __init__(self, op, term):
        self.token = self.op = op
        self.term = term


class NoOp(AST):
    """
    represent an empty statement
    """
    pass


class RelOp(AST):
    """
    Represent a relational operator
    Ex: x <= y
    """

    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right


class Assign(AST):
    """
    Represent assign operator: ident ":=" expression
    Ex: x := y
    """

    def __init__(self, identifier, expression):
        self.identifier = identifier
        self.expression = expression


class Call(AST):
    """
    Represent "call" keyword
    """

    def __init__(self, identifier):
        self.identifier = identifier
        # a reference to procedure declaration symbol
        self.proc_symbol = None


class Odd(AST):
    """
    Represent "odd" keyword
    """

    def __init__(self, expression):
        self.expression = expression


class Read(AST):
    """
    Represent "read" keyword
    """

    def __init__(self, identifier):
        self.identifier = identifier


class Write(AST):
    """
    Represent "write" keyword
    """

    def __init__(self, expression):
        self.expression = expression


class BeginEnd(AST):
    """
    Represent "begin" statement {";" statement } "end"
    """

    def __init__(self, statement_list):
        self.statement_list = statement_list


class If(AST):
    """
    Represent "if" condition "then" statement
    """

    def __init__(self, condition, statement):
        self.condition = condition
        self.statement = statement


class While(AST):
    """
    Represent "while" condition "do" statement
    """

    def __init__(self, condition, statement):
        self.condition = condition
        self.statement = statement


class VarDec(AST):
    """
    Represent "var" declaration
    Ex: "var" ident {"," ident} ";"
    """

    def __init__(self, ident_list):
        self.ident_list = ident_list


class ProcDec(AST):
    """
    Represent a Procedure
    Ex: "procedure" ident ";" block ";"
    """

    def __init__(self, identifier, block):
        self.identifier = identifier
        self.block = block


class Block(AST):
    """
    Represent a block
    Ex: block = const_declaration var_declaration procedure statement
    """

    def __init__(self, var_declaration, procedure_declaration_list, statement):
        self.var_declaration = var_declaration
        self.procedure_declaration_list = procedure_declaration_list
        self.statement = statement


class Program(AST):
    """
    Represent a Program
    """

    def __init__(self, block):
        self.block = block
