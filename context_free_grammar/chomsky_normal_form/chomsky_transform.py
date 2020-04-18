from context_free_grammar.simplicification.remove_useless_symbols import RemoveUselessSymbols
from context_free_grammar.simplicification.remove_null import RemoveNull
from context_free_grammar.simplicification.remove_unit import RemoveUnit
import context_free_grammar.tools.function as function
import string


class ChomskyTransform:
    """Chomsky's Normal Form"""

    def __init__(self, grammar):
        self.grammar = grammar

    def check_production_rule(self):
        """
        Check production rules: RHS of the production if they exist with other non-terminals or terminals
        Ex: if:
                S -> aA
            then:
                a_N -> a
                S -> a_NA
        """
        list_terminal = []
        list_index = []
        for i in range(len(self.grammar.production_rules)):
            if function.intersection(self.grammar.production_rules[i].right_side, self.grammar.non_terminal) and \
                    function.intersection(self.grammar.production_rules[i].right_side, self.grammar.terminal):
                list_index.append(i)
                list_tmp = function.intersection(self.grammar.production_rules[i].right_side, self.grammar.terminal)
                for j in range(len(list_tmp)):
                    if list_tmp[j] not in list_terminal:
                        list_terminal.append(list_tmp[j])

        return list_terminal, list_index

    def transform(self):
        # Step 1: Eliminate start symbol from the RHS
        self.grammar.set_production_rules('S0', self.grammar.get_start_symbol())
        self.grammar.set_start_symbol('S0')

        self.grammar.setting()

        # Step 2: Removing the null, unit and useless productions
        remove_null = RemoveNull(self.grammar)
        remove_null.transform()
        remove_unit = RemoveUnit(self.grammar)
        remove_unit.transform()
        remove_useless_symbols = RemoveUselessSymbols(self.grammar)
        remove_useless_symbols.transform()

        self.grammar.setting()

        # Step 3: Eliminate terminals from the RHS of the production if they exist with other non-terminals or terminals
        list_terminal, list_index = self.check_production_rule()
        symbol_replace = string.ascii_uppercase
        dict_replace_step_3 = {}

        for i in range(len(list_terminal)):
            for j in range(len(symbol_replace)):
                if symbol_replace[j] not in self.grammar.non_terminal and \
                        symbol_replace[j] not in dict_replace_step_3.values():
                    dict_replace_step_3[list_terminal[i]] = symbol_replace[j]
                    break

        for k, v in dict_replace_step_3.items():
            self.grammar.set_production_rules(v, k)

        for i in range(len(self.grammar.production_rules)):
            if i in list_index:
                right_side_of_rule_i = self.grammar.production_rules[i].right_side
                for j in range(len(right_side_of_rule_i)):
                    if right_side_of_rule_i[j] in list_terminal:
                        right_side_of_rule_i = right_side_of_rule_i.replace(
                            right_side_of_rule_i[j],
                            dict_replace_step_3[right_side_of_rule_i[j]]
                        )

                        self.grammar.modify_production_rule(i, right_side_of_rule_i)

        self.grammar.setting()

        # Step 4: Eliminate RHS with more than two non-terminals
        dict_replace_step_4 = {}

        for i in range(len(self.grammar.production_rules)):
            right_side_of_rule_i = self.grammar.production_rules[i].right_side

            while function.intersection(list(right_side_of_rule_i), self.grammar.non_terminal) and \
                    len(right_side_of_rule_i) > 2:

                if right_side_of_rule_i[0:2] not in dict_replace_step_4.keys():
                    for j in range(len(symbol_replace)):
                        if symbol_replace[j] not in self.grammar.non_terminal and \
                                symbol_replace[j] not in dict_replace_step_4.values():
                            dict_replace_step_4[right_side_of_rule_i[0:2]] = symbol_replace[j]
                            break

                right_side_of_rule_i = function.replace(
                    right_side_of_rule_i,
                    dict_replace_step_4[right_side_of_rule_i[0:2]]
                )

                self.grammar.modify_production_rule(i, right_side_of_rule_i)

        for k, v in dict_replace_step_4.items():
            self.grammar.set_production_rules(v, k)

        self.grammar.setting()
