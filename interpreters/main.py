from lexer_analysis.lexer.lexer import Lexer
from syntax_analysis_ast.parser.parser import Parser
from interpreters.interpreter.interpreter import Interpreter
from semantic_analysis.semantic.semantic import Semantic

file = open('library/input.txt', 'r')
lexer = Lexer(file.read())

tokens = lexer.tokenize()

parser = Parser(tokens)

tree = parser.parse()
print('\n')
print('-' * 30)
print('Semantic analysis:')
semantic = Semantic()
try:
    semantic.visit(tree)
except Exception as e:
    print(e)

print('\n')
print('-' * 30)
print('Interpreter:')
interpreter = Interpreter(tree)

result = interpreter.interpret()
# print('\n')
# print('result = ' + str(result))
#
# print('\n')
# print('Run-time GLOBAL_MEMORY contents:')
# for k, v in sorted(interpreter.GLOBAL_SCOPE.items()):
#     print('{} = {}'.format(k, v))
