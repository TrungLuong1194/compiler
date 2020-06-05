import context_free_grammar.tools.function as function


class RemoveNull:
    """Elimination of ε Production"""

    def __init__(self, grammar):
        self.grammar = grammar

    def transform(self):
        # Return a list: left side of rules, which have right side = 'e'
        # Ex: A --> ['e'], B --> ['e'] => return ['A', 'B']
        e_list = []

        for i in range(len(self.grammar.rule)):
            if self.grammar.rule[i].right_side == ['e'] and \
                    self.grammar.rule[i].left_side not in e_list:
                e_list.append(self.grammar.rule[i].left_side)

        flag = True
        while flag:
            flag = False
            for i in range(len(self.grammar.rule)):
                if e_list == self.grammar.rule[i].right_side and self.grammar.rule[i].left_side not in e_list:
                    e_list.append(self.grammar.rule[i].left_side)
                    flag = True

        self.grammar.remove_production_rule_by_e()
        self.grammar.remove_terminal_e()

        for ele in e_list:
            for index in range(len(self.grammar.rule)):

                if ele in self.grammar.rule[index].right_side:
                    # Return right side list, which have left side = left side of rule index
                    right_side_of_rule_index = []

                    for i in range(len(self.grammar.rule)):
                        if self.grammar.rule[i].left_side == self.grammar.rule[index].left_side:
                            right_side_of_rule_index.append(self.grammar.rule[i].right_side)

                    # Return index of ele in right side of rule
                    # Ex: ele = A, right side of rule = 'ABA' => return [0, 2]
                    index_in_right_side = [i for i, v in enumerate(self.grammar.rule[index].right_side) if v == ele]

                    combination_index_in_right_side = function.combinations_list(index_in_right_side)

                    new_right_side = function.remove_list(
                        self.grammar.rule[index].right_side,
                        combination_index_in_right_side
                    )

                    # add new rule
                    for i in new_right_side:
                        # if i not null and i not in right side and i not equal left side
                        if i and i not in right_side_of_rule_index:
                            if len(i) == 1 and i[0] == self.grammar.rule[index].left_side:
                                pass
                            else:
                                self.grammar.add_production_rules(self.grammar.rule[index].left_side, i)
