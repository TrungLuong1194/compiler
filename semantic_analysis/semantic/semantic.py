from semantic_analysis.node_visitor.node_visitor import NodeVisitor
from semantic_analysis.symbol_table.symbol_table import SymbolTable
from semantic_analysis.symbol_table.symbol import Symbol


class Semantic(NodeVisitor):
    def __init__(self):
        self.symtab = SymbolTable()

    def visit_Number(self, node):
        pass

    def visit_Identifier(self, node):
        symbol = Symbol(node.value)
        symbol_find = self.symtab.lookup(symbol)
        if symbol_find is None:
            raise Exception("Can't find '" + symbol.name + "'")

    def visit_BinOp(self, node):
        self.visit(node.left)
        self.visit(node.right)

    def visit_UnaryOp(self, node):
        self.visit(node.term)

    def visit_NoOp(self, node):
        pass

    def visit_RelOp(self, node):
        self.visit(node.left)
        self.visit(node.right)

    def visit_Assign(self, node):
        self.visit(node.identifier)
        self.visit(node.expression)

    def visit_Call(self, node):
        pass

    def visit_Odd(self, node):
        pass

    def visit_Read(self, node):
        pass

    def visit_Write(self, node):
        self.visit(node.expression)

    def visit_BeginEnd(self, node):
        for ele in node.statement_list:
            self.visit(ele)

    def visit_If(self, node):
        self.visit(node.condition)
        self.visit(node.statement)

    def visit_While(self, node):
        self.visit(node.condition)
        self.visit(node.statement)

    def visit_VarDec(self, node):
        for ident in node.ident_list:
            symbol = Symbol(ident.value)

            symbol_find = self.symtab.lookup(symbol)
            if symbol_find is not None:
                raise Exception("Duplicate identifier '" + symbol.name + "'")

            self.symtab.define(symbol)

    def visit_Procedure(self, node):
        pass

    def visit_Block(self, node):
        self.visit(node.var_declaration)
        self.visit(node.procedure_declaration)
        self.visit(node.statement)

    def visit_Program(self, node):
        self.visit(node.block)
