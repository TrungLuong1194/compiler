from context_free_grammar.grammar_settings.grammar import Grammar
from context_free_grammar.chomsky_normal_form.chomsky_transform import ChomskyTransform
from context_free_grammar.tools.write_xml import WriteXml
from syntax_analysis.first import First
from syntax_analysis.follow import Follow
import xml.etree.ElementTree as elementTree

# import xml data
tree = elementTree.parse('input.xml')
root = tree.getroot()

# setting grammar
grammar = Grammar()

grammar.setting(root)
grammar.display()

# first rule
first = First(grammar)

print('-' * 50)
print('First Sets:')
first_set = first.transform()

for i, v in first_set.items():
    print('First<' + str(i) + '> : ' + str(v))

# first rule
follow = Follow(grammar, first_set)

print('-' * 50)
print('Follow Sets:')
follow_set = follow.transform()

for i, v in follow_set.items():
    print('Follow<' + str(i) + '> : ' + str(v))
