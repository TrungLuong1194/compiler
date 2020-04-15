import context_free_grammar.tools.function as function


class RemoveUselessSymbols:
    """Removal of useless symbols"""

    def __init__(self, grammar):
        self.grammar = grammar
        self.derivation_list = []
        self.reachable_list = []

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

        self.grammar.set_non_terminal()
        self.grammar.set_terminal()

        for i in range(len(self.grammar.production_rules)):
            for j in list(self.grammar.production_rules[i].right_side):
                if j not in self.reachable_list:
                    self.reachable_list.append(j)

        for i in range(len(self.grammar.non_terminal)):
            if self.grammar.non_terminal[i] not in self.reachable_list:
                self.grammar.remove_production_rule(self.grammar.non_terminal[i])

        self.grammar.set_non_terminal()
        self.grammar.set_terminal()
