class RemoveUnit:
    """Removing unit productions"""

    def __init__(self, grammar):
        self.grammar = grammar

    def transform(self):
        flag = True
        while flag:
            flag = False

            for index in range(len(self.grammar.rule)):
                if self.grammar.rule[index].left_side != self.grammar.get_start_symbol() and \
                        len(self.grammar.rule[index].right_side) == 1 and \
                        self.grammar.rule[index].right_side[0] in self.grammar.non_terminal:
                    unit_element = self.grammar.rule[index].right_side[0]

                    flag = True
                    self.grammar.remove_production_rule_by_unit(unit_element)

                    # Return right side list, which have left side = left side of rule index
                    right_side_of_rule_index = []
                    for i in range(len(self.grammar.rule)):
                        if self.grammar.rule[i].left_side == self.grammar.rule[index].left_side:
                            right_side_of_rule_index.append(self.grammar.rule[i].right_side)

                    # Return right side list, which have left side = unit element
                    right_side_of_unit = []
                    for i in range(len(self.grammar.rule)):
                        if self.grammar.rule[i].left_side == unit_element:
                            right_side_of_unit.append(self.grammar.rule[i].right_side)

                    # add new rule
                    for ele in right_side_of_unit:
                        # if ele not in right side of rule index and ele not equal left side
                        if ele not in right_side_of_rule_index:
                            if len(ele) == 1 and ele[0] == self.grammar.rule[index].left_side:
                                pass
                            else:
                                self.grammar.add_production_rules(self.grammar.rule[index].left_side, ele)

                    break
