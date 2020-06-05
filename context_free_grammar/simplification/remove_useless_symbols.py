class RemoveUselessSymbols:
    """Removal of useless symbols"""

    def __init__(self, grammar):
        self.grammar = grammar

    def transform(self):
        # return a list: all right side
        # Ex: A --> ['B'], B --> ['c', 'A'] => return [['B'], ['c', 'A']]
        all_right_side = []

        for index in range(len(self.grammar.rule)):
            all_right_side = list(set().union(all_right_side, self.grammar.rule[index].right_side))

        # Case non-terminal never occur in right side of rules
        useless_list = []
        for index in range(len(self.grammar.rule)):
            if self.grammar.rule[index].left_side not in all_right_side:
                useless_list.append(self.grammar.rule[index].left_side)
                self.grammar.remove_terminal_useless(self.grammar.rule[index].left_side)

        self.grammar.remove_production_rule_by_useless_list(useless_list)

        # Case no way to terminate. Ex: A --> ['a', 'A']
        flag = True
        while flag:
            flag = False
            for index in range(len(self.grammar.rule)):
                if self.grammar.rule[index].left_side != self.grammar.get_start_symbol() and \
                        self.grammar.rule[index].left_side == self.grammar.rule[index].right_side[-1]:
                    useless_ele = self.grammar.rule[index].left_side

                    flag = True
                    self.grammar.remove_production_rule_by_useless(useless_ele)
                    self.grammar.remove_terminal_useless(useless_ele)

                    break
