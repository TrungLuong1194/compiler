from context_free_grammar.simplicification.remove_useless_symbols import RemoveUselessSymbols
from context_free_grammar.simplicification.remove_null import RemoveNull
from context_free_grammar.simplicification.remove_unit import RemoveUnit


class ChomskyTransform:
    """Chomsky's Normal Form"""

    def __init__(self, grammar):
        self.grammar = grammar

    def transform(self):
        # Step 1: Eliminate start symbol from the RHS
        self.grammar.set_production_rules('S0', self.grammar.get_start_symbol())
        self.grammar.set_start_symbol('S0')

        # Step 2: Removing the null, unit and useless productions
        remove_null = RemoveNull(self.grammar)
        remove_null.transform()

        remove_unit = RemoveUnit(self.grammar)
        remove_unit.transform()

        remove_useless_symbols = RemoveUselessSymbols(self.grammar)
        remove_useless_symbols.transform()

        self.grammar.setting()

