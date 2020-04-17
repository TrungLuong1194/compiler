from itertools import combinations
import context_free_grammar.tools.function as function


class RemoveNull:
    """Elimination of ε Production"""

    def __init__(self, grammar):
        self.grammar = grammar
        self.null_list = []

    def transform(self):
        for i in range(len(self.grammar.production_rules)):
            if self.grammar.production_rules[i].right_side == 'e' and \
                    self.grammar.production_rules[i].left_side not in self.null_list:
                self.null_list.append(self.grammar.production_rules[i].left_side)

        self.grammar.remove_production_rule_by_e()

        for i in range(len(self.null_list)):
            for j in range(len(self.grammar.production_rules)):
                right_side_of_rule_j = list(self.grammar.production_rules[j].right_side)

                if self.null_list[i] in right_side_of_rule_j:
                    list_right_side_of_left_symbol_of_rule_j = []
                    for k in range(len(self.grammar.production_rules)):
                        if self.grammar.production_rules[k].left_side == self.grammar.production_rules[j].left_side:
                            list_right_side_of_left_symbol_of_rule_j.append(self.grammar.production_rules[k].right_side)

                    index = []
                    for k in range(len(right_side_of_rule_j)):
                        if right_side_of_rule_j[k] == self.null_list[i]:
                            index.append(k)

                    union = []
                    for k in range(len(index)):
                        tmp = list(combinations(index, k + 1))
                        for t in range(len(tmp)):
                            union.append(tmp[t])

                    for k in range(len(union)):
                        new_right_side = function.remove_string_by_index(self.grammar.production_rules[j].right_side,
                                                                         union[k])
                        if new_right_side not in list_right_side_of_left_symbol_of_rule_j and new_right_side != '':
                            self.grammar.set_production_rules(self.grammar.production_rules[j].left_side,
                                                              new_right_side)

        self.grammar.setting()
