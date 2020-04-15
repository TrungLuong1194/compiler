from context_free_grammar.grammar_settings.transition import Transition


class Grammar:
    """Setting a grammar"""

    def __init__(self):
        self.non_terminal = None
        self.terminal = None
        self.production_rules = []
        self.start_symbol = None

    def set_non_terminal(self):
        self.non_terminal = []
        for i in range(len(self.production_rules)):
            if self.production_rules[i].left_side not in self.non_terminal:
                self.non_terminal.append(self.production_rules[i].left_side)

    def set_terminal(self):
        self.terminal = []
        for i in range(len(self.production_rules)):
            for j in self.production_rules[i].right_side:
                if j not in self.non_terminal and j not in self.terminal:
                    self.terminal.append(j)

    def set_production_rules(self, left_side, right_side):
        trans = Transition(left_side, right_side)
        self.production_rules.append(trans)

    def set_start_symbol(self, start_symbol):
        self.start_symbol = start_symbol

    def remove_production_rule(self, symbol):
        self.production_rules = [ele for ele in self.production_rules if ele.left_side != symbol]
        self.production_rules = [ele for ele in self.production_rules if symbol not in list(ele.right_side)]

    def remove_production_rule_by_e(self):
        self.production_rules = [ele for ele in self.production_rules if ele.right_side != 'e']

    def display(self):
        print('Nonterminal symbols: ' + str(len(self.non_terminal)))
        for i in range(len(self.non_terminal)):
            print(self.non_terminal[i])

        print('Terminal symbols: ' + str(len(self.terminal)))
        for i in range(len(self.terminal)):
            print(self.terminal[i])

        print('Production rules: ' + str(len(self.production_rules)))
        for i in range(len(self.production_rules)):
            print(str(self.production_rules[i].left_side) + ' ------> ' + str(self.production_rules[i].right_side))

        print('Start symbol:')
        print(self.start_symbol)
