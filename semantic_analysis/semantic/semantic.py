from semantic_analysis.node_visitor.node_visitor import NodeVisitor
from semantic_analysis.symbol_table.scoped_symbol_table import ScopedSymbolTable
from semantic_analysis.symbol_table.symbol import Symbol


class Semantic(NodeVisitor):
    def __init__(self):
        self.current_scope = None

    def visit_Number(self, node):
        pass

    def visit_Identifier(self, node):
        symbol = Symbol(node.value)
        symbol_find = self.current_scope.lookup(symbol)
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
            symbol = Symbol(ident.value, 'variable')

            symbol_find = self.current_scope.lookupCurrent(symbol)
            if symbol_find is not None:
                raise Exception("Duplicate identifier '" + symbol.name + "'")

            self.current_scope.define(symbol)

    def visit_ProcDec(self, node):
        ident = node.identifier
        symbol = Symbol(ident.value, 'procedure')
        self.current_scope.define(symbol)

        print('ENTER scope: ' + str(ident.value))
        # Scope for parameters and local variables
        procedure_scope = ScopedSymbolTable(ident.value, self.current_scope.scope_level + 1, self.current_scope)
        self.current_scope = procedure_scope

        self.visit(node.block)

        procedure_scope.display()

        self.current_scope = self.current_scope.enclosing_scope

        print('\n')
        print('LEAVE scope: ' + str(ident.value))

    def visit_Block(self, node):
        self.visit(node.var_declaration)
        for ele in node.procedure_declaration_list:
            self.visit(ele)
        self.visit(node.statement)

    def visit_Program(self, node):
        print('ENTER scope: global')
        global_scope = ScopedSymbolTable('global', 1, self.current_scope)
        self.current_scope = global_scope

        self.visit(node.block)

        global_scope.display()

        self.current_scope = self.current_scope.enclosing_scope

        print('\n')
        print('LEAVE scope: global')
