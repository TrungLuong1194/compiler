from context_free_grammar.grammar_settings.grammar import Grammar
from context_free_grammar.simplicification.remove_useless_symbols import RemoveUselessSymbols

grammar = Grammar()

grammar.set_production_rules('T', 'aaB')
grammar.set_production_rules('T', 'abA')
grammar.set_production_rules('T', 'aaT')
grammar.set_production_rules('A', 'aA')
grammar.set_production_rules('B', 'ab')
grammar.set_production_rules('B', 'b')
grammar.set_production_rules('C', 'ad')
grammar.set_non_terminal()
grammar.set_terminal()
grammar.set_start_symbol('T')

grammar.display()

print('-' * 60)
print('Remove useless symbols:\n')

remove_useless_symbols = RemoveUselessSymbols(grammar)
remove_useless_symbols.transform()

grammar.display()
