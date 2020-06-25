from lexer_analysis.lexer.lexer import Lexer
from syntax_analysis_ast.parser.parser import Parser
from interpreter_step.interpreter import Interpreter

file = open('library/input.txt', 'r')
lexer = Lexer(file.read())

tokens = lexer.tokenize()

parser = Parser(tokens)

interpreter = Interpreter(parser)

result = interpreter.interpret()
print('\n')
print('result = ' + str(result))

print('\n')
print('Run-time GLOBAL_MEMORY contents:')
for k, v in sorted(interpreter.GLOBAL_SCOPE.items()):
    print('{} = {}'.format(k, v))
