from lexer_analysis.lexer.lexer import Lexer
from syntax_analysis_ast.parser.parser import Parser
from semantic_analysis.symbol_table.symbol_table_builder import SymbolTableBuilder

file = open('library/input.txt', 'r')
lexer = Lexer(file.read())

tokens = lexer.tokenize()

parser = Parser(tokens)
tree = parser.parse()

symtab_builder = SymbolTableBuilder()
symtab_builder.visit(tree)
