from lexer_analysis.lexer.lexer import Lexer

file = open('input.py', 'r')

lexer = Lexer(file.read())
tokens = lexer.tokenize()

for i in tokens:
    i.display()
