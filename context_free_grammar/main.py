from context_free_grammar.grammar_settings.grammar import Grammar
from context_free_grammar.chomsky_normal_form.chomsky_transform import ChomskyTransform

grammar = Grammar()

grammar.set_production_rules('T', 'aaBaaB')
grammar.set_production_rules('T', 'abA')
grammar.set_production_rules('T', 'aaT')
grammar.set_production_rules('A', 'aA')
grammar.set_production_rules('B', 'ab')
grammar.set_production_rules('B', 'b')
grammar.set_production_rules('C', 'ad')
grammar.set_production_rules('B', 'e')
grammar.set_production_rules('A', 'e')
grammar.set_production_rules('E', 'e')

grammar.setting()
grammar.set_start_symbol('T')
grammar.display()

print('-' * 80)
print("Chomsky's Normal Form:\n")

chomsky_transform = ChomskyTransform(grammar)
chomsky_transform.transform()
grammar.display()