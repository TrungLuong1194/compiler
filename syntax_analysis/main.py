from context_free_grammar.grammar_settings.grammar import Grammar
from syntax_analysis.LL1.first import First
from syntax_analysis.LL1.follow import Follow
from syntax_analysis.LL1.parse_table import ParseTable
from syntax_analysis.parser.parser import Parser
import xml.etree.ElementTree as elementTree

# import xml data
tree = elementTree.parse('input.xml')
root = tree.getroot()

# setting grammar
grammar = Grammar()

grammar.setting(root)
grammar.display()

# first set
first = First(grammar)

print('-' * 50)
print('First Sets:')
first_set, parse_table = first.transform()

for i, v in first_set.items():
    print('First<' + str(i) + '> : ' + str(v))

# follow set
follow = Follow(grammar, first_set)

print('-' * 50)
print('Follow Sets:')
follow_set = follow.transform()

for i, v in follow_set.items():
    print('Follow<' + str(i) + '> : ' + str(v))

# parse table
print('-' * 50)
print('Parse Table:')

parse_table = ParseTable(grammar)
df, parse_table = parse_table.transform()
print(df)
print(parse_table)

# parser transform
print('-' * 50)
print('Parse Transform:')

parser = Parser(grammar, parse_table)
parser.transform('i+i*i')
