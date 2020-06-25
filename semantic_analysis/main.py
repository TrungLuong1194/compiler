from lexer_analysis.lexer.lexer import Lexer
from syntax_analysis_ast.parser.parser import Parser
from semantic_analysis.semantic.semantic import Semantic

file = open('library/input.txt', 'r')
lexer = Lexer(file.read())
tokens = lexer.tokenize()

parser = Parser(tokens)
tree = parser.parse()

semantic = Semantic()
try:
    semantic.visit(tree)
except Exception as e:
    print(e)

semantic.symtab.display()
