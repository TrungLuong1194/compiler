class RemoveUnit:
    """Removing unit productions"""

    def __init__(self, grammar):
        self.grammar = grammar

    def transform(self):
        flag = True
        while flag:
            flag = False
            symbol = None
            for i in range(len(self.grammar.production_rules)):
                if self.grammar.production_rules[i].right_side in self.grammar.non_terminal:
                    flag = True
                    list_right_side_of_left_symbol_of_rule_i = []

                    for j in range(len(self.grammar.production_rules)):
                        if self.grammar.production_rules[j].left_side == self.grammar.production_rules[i].left_side:
                            list_right_side_of_left_symbol_of_rule_i.append(self.grammar.production_rules[j].right_side)

                    symbol = self.grammar.production_rules[i].right_side
                    right_side_of_rule_i = []

                    for j in range(len(self.grammar.production_rules)):
                        if self.grammar.production_rules[j].left_side == symbol:
                            right_side_of_rule_i.append(self.grammar.production_rules[j].right_side)

                    for j in range(len(right_side_of_rule_i)):
                        if right_side_of_rule_i[j] not in list_right_side_of_left_symbol_of_rule_i:
                            self.grammar.set_production_rules(self.grammar.production_rules[i].left_side,
                                                              right_side_of_rule_i[j])

                    break
            if symbol:
                self.grammar.remove_production_rule_by_unit(symbol)

        self.grammar.setting()
