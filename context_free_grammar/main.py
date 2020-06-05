from context_free_grammar.grammar_settings.grammar import Grammar
from context_free_grammar.chomsky_normal_form.chomsky_transform import ChomskyTransform
from context_free_grammar.tools.write_xml import WriteXml
import xml.etree.ElementTree as elementTree

# import xml data
tree = elementTree.parse('input.xml')
root = tree.getroot()

# setting grammar
grammar = Grammar()

grammar.setting(root)
grammar.display()

# display Chomsky's
print('-' * 80)
print("Chomsky's Normal Form:\n")

chomsky_transform = ChomskyTransform(grammar)
chomsky_transform.transform()
grammar.display()

# output file xml
xml = WriteXml(grammar)
xml.write()


