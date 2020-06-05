from context_free_grammar.grammar_settings.grammar import Grammar
from context_free_grammar.chomsky_normal_form.chomsky_transform import ChomskyTransform
import xml.etree.ElementTree as elementTree

from context_free_grammar.simplification.remove_null import RemoveNull
from context_free_grammar.simplification.remove_unit import RemoveUnit

# import xml data
tree = elementTree.parse('input.xml')
root = tree.getroot()

# setting grammar
grammar = Grammar()

grammar.setting(root)
grammar.display()



print('-' * 50)
print('\n')
print('RemoveNull:\n')
removeNull = RemoveNull(grammar)
removeNull.transform()
grammar.display()


print('-' * 50)
print('\n')
print('RemoveUnit:\n')
removeUnit = RemoveUnit(grammar)
removeUnit.transform()
grammar.display()




# print('-' * 80)
# print("Chomsky's Normal Form:\n")
#
# chomsky_transform = ChomskyTransform(grammar)
# chomsky_transform.transform()
# grammar.display()
