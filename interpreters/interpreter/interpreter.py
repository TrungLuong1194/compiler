from lexer_analysis.token.tokentype import TokenType
from semantic_analysis.node_visitor.node_visitor import NodeVisitor
from interpreters.tools.call_stack import CallStack
from interpreters.tools.activation_record import ActivationRecord
from interpreters.tools.artype import ARType


class Interpreter(NodeVisitor):
    def __init__(self, tree):
        self.tree = tree
        self.call_stack = CallStack()

    def visit_Number(self, node):
        return node.value

    def visit_Identifier(self, node):
        ar = self.call_stack.peek()

        return ar.get(node.value)

    def visit_BinOp(self, node):
        if node.op.typeToken == TokenType.Plus.name:
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.typeToken == TokenType.Minus.name:
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.typeToken == TokenType.Mul.name:
            return self.visit(node.left) * self.visit(node.right)
        elif node.op.typeToken == TokenType.Div.name:
            return self.visit(node.left) / self.visit(node.right)

    def visit_UnaryOp(self, node):
        if node.op.typeToken == TokenType.Plus.name:
            return +self.visit(node.term)
        elif node.op.typeToken == TokenType.Minus.name:
            return -self.visit(node.term)

    def visit_NoOp(self, node):
        pass

    def visit_RelOp(self, node):
        if node.op.typeToken == TokenType.Greater.name:
            if self.visit(node.left) > self.visit(node.right):
                return True
            else:
                return False
        elif node.op.typeToken == TokenType.GreaterOrEqual.name:
            if self.visit(node.left) > self.visit(node.right) or self.visit(node.left) == self.visit(node.right):
                return True
            else:
                return False
        elif node.op.typeToken == TokenType.Less.name:
            if self.visit(node.left) < self.visit(node.right):
                return True
            else:
                return False
        elif node.op.typeToken == TokenType.LessOrEqual.name:
            if self.visit(node.left) < self.visit(node.right) or self.visit(node.left) == self.visit(node.right):
                return True
            else:
                return False
        elif node.op.typeToken == TokenType.NotEqual.name:
            if self.visit(node.left) != self.visit(node.right):
                return True
            else:
                return False
        elif node.op.typeToken == TokenType.Equal.name:
            if self.visit(node.left) == self.visit(node.right):
                return True
            else:
                return False

    def visit_Assign(self, node):
        ar = self.call_stack.peek()

        ar[node.identifier.value] = self.visit(node.expression)

    def visit_Call(self, node):
        pass

    def visit_Odd(self, node):
        pass

    def visit_Read(self, node):
        pass

    def visit_Write(self, node):
        # print(self.visit(node.expression))
        pass

    def visit_BeginEnd(self, node):
        for ele in node.statement_list:
            self.visit(ele)

    def visit_If(self, node):
        if self.visit(node.condition):
            return self.visit(node.statement)

    def visit_While(self, node):
        while self.visit(node.condition):
            self.visit(node.statement)

    def visit_VarDec(self, node):
        pass

    def visit_ProcDec(self, node):
        pass

    def visit_Block(self, node):
        self.visit(node.var_declaration)
        for ele in node.procedure_declaration_list:
            self.visit(ele)
        self.visit(node.statement)

    def visit_Program(self, node):
        print('ENTER: PROGRAM')

        ar = ActivationRecord(name='program', type=ARType.PROGRAM, nesting_level=1)
        self.call_stack.push(ar)

        print(self.call_stack)

        self.visit(node.block)

        print('LEAVE: PROGRAM')
        print(self.call_stack)

        self.call_stack.pop()

    def interpret(self):
        tree = self.tree

        if tree is None:
            return ''

        return self.visit(tree)
