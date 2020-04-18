from context_free_grammar.grammar_settings.grammar import Grammar
from context_free_grammar.chomsky_normal_form.chomsky_transform import ChomskyTransform

grammar = Grammar()

grammar.set_production_rules('S', 'ASB')
grammar.set_production_rules('A', 'aAS')
grammar.set_production_rules('A', 'a')
grammar.set_production_rules('A', 'e')
grammar.set_production_rules('B', 'SbS')
grammar.set_production_rules('B', 'A')
grammar.set_production_rules('B', 'bb')

grammar.setting()
grammar.set_start_symbol('S')
grammar.display()

print('-' * 80)
print("Chomsky's Normal Form:\n")

chomsky_transform = ChomskyTransform(grammar)
chomsky_transform.transform()
grammar.display()
