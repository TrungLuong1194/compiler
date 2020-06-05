from context_free_grammar.simplification.remove_null import RemoveNull
from context_free_grammar.simplification.remove_unit import RemoveUnit
import context_free_grammar.tools.function as function
import string


class ChomskyTransform:
    """Chomsky's Normal Form"""

    def __init__(self, grammar):
        self.grammar = grammar

    def check_production_rule_step_3(self):
        """
        Check production rules: RHS of the production if they exist with other non-terminals or terminals.
        ['a', 'A'] or ['a', 'a']
        """
        list_terminal = []
        list_index = []

        for i in range(len(self.grammar.rule)):
            # Check ['a', 'A']
            if function.intersection(self.grammar.rule[i].right_side, self.grammar.non_terminal) and \
                    function.intersection(self.grammar.rule[i].right_side, self.grammar.terminal):
                list_index.append(i)

            # Check ['a', 'a']
            if not function.intersection(self.grammar.rule[i].right_side, self.grammar.non_terminal) and \
                    len(self.grammar.rule[i].right_side) > 1:
                list_index.append(i)

            list_tmp = function.intersection(self.grammar.rule[i].right_side, self.grammar.terminal)
            for j in range(len(list_tmp)):
                if list_tmp[j] not in list_terminal:
                    list_terminal.append(list_tmp[j])

        return list_terminal, list_index

    def transform(self):
        # Step 1: Eliminate start symbol from the RHS
        self.grammar.add_production_rules('S0', list(self.grammar.get_start_symbol()))
        self.grammar.add_non_terminal('S0')
        self.grammar.update_start_symbol('S0')

        # Step 2: Removing the null, unit and useless productions
        remove_null = RemoveNull(self.grammar)
        remove_null.transform()

        remove_unit = RemoveUnit(self.grammar)
        remove_unit.transform()

        symbol_replace = string.ascii_uppercase  # Return string "AB...Z"
        # Step 3: Eliminate terminals from the RHS of the production if they exist with other non-terminals or terminals
        list_terminal, list_index = self.check_production_rule_step_3()

        # S --> ['a', 'A'] => aN --> ['a'], S --> ['aN', 'A']
        for ele in list_terminal:

            for s in range(len(symbol_replace)):
                if symbol_replace[s] not in self.grammar.non_terminal:
                    self.grammar.add_production_rules(symbol_replace[s], list(ele))
                    self.grammar.add_non_terminal(symbol_replace[s])

                    for i in list_index:
                        for j in range(len(self.grammar.rule[i].right_side)):
                            if self.grammar.rule[i].right_side[j] == ele:
                                self.grammar.rule[i].right_side[j] = symbol_replace[s]

                    break

        # Step 4: Eliminate RHS with more than two non-terminals
        tmp = []  # store right side need replace
        data = {}  # store value replaced

        for i in range(len(self.grammar.rule)):
            while function.intersection(self.grammar.rule[i].right_side, self.grammar.non_terminal) and len(
                    self.grammar.rule[i].right_side) > 2:
                if self.grammar.rule[i].right_side[0:2] not in tmp:
                    tmp.append(self.grammar.rule[i].right_side[0:2])

                    for s in range(len(symbol_replace)):
                        if symbol_replace[s] not in self.grammar.non_terminal:
                            data[symbol_replace[s]] = self.grammar.rule[i].right_side[0:2]

                            self.grammar.add_production_rules(symbol_replace[s], self.grammar.rule[i].right_side[0:2])
                            self.grammar.add_non_terminal(symbol_replace[s])

                            self.grammar.rule[i].right_side = \
                                list(symbol_replace[s]) + \
                                self.grammar.rule[i].right_side[2:]

                            break
                else:
                    self.grammar.rule[i].right_side = \
                        [k for k, v in data.items() if v == self.grammar.rule[i].right_side[0:2]] \
                        + self.grammar.rule[i].right_side[2:]
