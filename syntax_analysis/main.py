from context_free_grammar.grammar_settings.grammar import Grammar
from syntax_analysis.LL1.first import First
from syntax_analysis.LL1.follow import Follow
from syntax_analysis.LL1.parse_table import ParseTable
from syntax_analysis.parser.parser import Parser
from lexer_analysis.lexer.lexer import Lexer
import xml.etree.ElementTree as elementTree

# import xml data
tree = elementTree.parse('CMinusGrammar.xml')
root = tree.getroot()

# setting grammar
print('-' * 80)
print('Grammars:')
print('-' * 80)

grammar = Grammar()

grammar.setting(root)
grammar.display()

# first set
first = First(grammar)

print('-' * 80)
print('First Sets:')
print('-' * 80)

first_set, parse_table = first.transform()

for i, v in first_set.items():
    print('First<' + str(i) + '> : ' + str(v))

# follow set
follow = Follow(grammar, first_set)

print('-' * 80)
print('Follow Sets:')
print('-' * 80)

follow_set = follow.transform()

for i, v in follow_set.items():
    print('Follow<' + str(i) + '> : ' + str(v))

# parse table
print('-' * 80)
print('Parse Table:')
print('-' * 80)

parse_table = ParseTable(grammar)
df, parse_table = parse_table.transform()
print(df)
# print(parse_table)

# parser transform
print('-' * 80)
print('Parse Transform:')
print('-' * 80)

file = open('input.c', 'r')

lexer = Lexer(file.read())
tokens = lexer.tokenize()

parser = Parser(grammar, parse_table, tokens)
parser.transform()
