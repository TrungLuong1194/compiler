import context_free_grammar.tools.function as function


class RemoveUselessSymbols:
    """Removal of useless symbols"""

    def __init__(self, grammar):
        self.grammar = grammar
        self.derivation_list = []
        self.reachable_list = [self.grammar.get_start_symbol()]

    def transform(self):
        for i in self.grammar.terminal:
            self.derivation_list.append(i)

        flag = True
        while flag:
            flag = False
            for i in range(len(self.grammar.production_rules)):
                if self.grammar.production_rules[i].left_side not in self.derivation_list and function.is_child_list(
                        list(self.grammar.production_rules[i].right_side), self.derivation_list):
                    self.derivation_list.append(self.grammar.production_rules[i].left_side)
                    flag = True

        for i in range(len(self.grammar.non_terminal)):
            if self.grammar.non_terminal[i] not in self.derivation_list:
                self.grammar.remove_production_rule(self.grammar.non_terminal[i])

        self.grammar.setting()

        for i in range(len(self.grammar.production_rules)):
            if self.grammar.production_rules[i].left_side == self.grammar.get_start_symbol():
                right_side_of_start_symbol = list(self.grammar.production_rules[i].right_side)
                for j in range(len(right_side_of_start_symbol)):
                    if right_side_of_start_symbol[j] not in self.reachable_list:
                        self.reachable_list.append(right_side_of_start_symbol[j])

        for i in range(len(self.grammar.production_rules)):
            if self.grammar.production_rules[i].left_side in self.reachable_list:
                right_side_of_rule_i = list(self.grammar.production_rules[i].right_side)
                for j in range(len(right_side_of_rule_i)):
                    if right_side_of_rule_i[j] not in self.reachable_list:
                        self.reachable_list.append(right_side_of_rule_i[j])

        for i in range(len(self.grammar.non_terminal)):
            if self.grammar.non_terminal[i] not in self.reachable_list:
                self.grammar.remove_production_rule(self.grammar.non_terminal[i])

        self.grammar.setting()
