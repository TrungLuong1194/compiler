from lexer_analysis.lexer.lexer import Lexer
from syntax_analysis_ast.parser.parser import Parser

file = open('library/input.txt', 'r')
lexer = Lexer(file.read())
tokens = lexer.tokenize()

parser = Parser(tokens)
tree = parser.parse()
