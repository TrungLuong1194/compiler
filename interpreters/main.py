from lexer_analysis.lexer.lexer import Lexer
from syntax_analysis_ast.parser.parser import Parser
from interpreters.interpreter.interpreter import Interpreter
from semantic_analysis.semantic.semantic import Semantic

file = open('library/input.txt', 'r')

print('-' * 80)
print('Lexical analysis:')
print('-' * 80)
lexer = Lexer(file.read())
tokens = lexer.tokenize()

for i in tokens:
    i.display()

print('\n')
print('-' * 80)
print('Syntax analysis:')
print('-' * 80)
parser = Parser(tokens)
tree = parser.parse()

print('\n')
print('-' * 80)
print('Semantic analysis:')
print('-' * 80)
semantic = Semantic()
semantic.visit(tree)
# try:
#     semantic.visit(tree)
# except Exception as e:
#     print(e)

print('\n')
print('-' * 80)
print('Interpreter:')
print('-' * 80)
interpreter = Interpreter(tree)

result = interpreter.interpret()
