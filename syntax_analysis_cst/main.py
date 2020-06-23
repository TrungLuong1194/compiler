from context_free_grammar.grammar_settings.grammar import Grammar
from syntax_analysis_cst.LL1.first import First
from syntax_analysis_cst.LL1.follow import Follow
from syntax_analysis_cst.LL1.parse_table import ParseTable
from syntax_analysis_cst.parser.parser import Parser
from lexer_analysis.lexer.lexer import Lexer
import xml.etree.ElementTree as elementTree

# import xml data
tree = elementTree.parse('library/PL0Grammar.xml')
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
# for i, v in parse_table.items():
#     print(str(i) + '-' + str(v))

# parser transform
print('-' * 80)
print('Parse Transform:')
print('-' * 80)

file = open('library/input.txt', 'r')

lexer = Lexer(file.read())
tokens = lexer.tokenize()

parser = Parser(grammar, parse_table, tokens)
syntax_tree = parser.transform()

print('\n')
print('-- Parser tree:')
for ele in syntax_tree:
    print(ele)
