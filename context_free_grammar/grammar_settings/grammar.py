from context_free_grammar.grammar_settings.transition import Transition


class Grammar:
    """Setting a grammar"""

    def __init__(self):
        self.non_terminal = None
        self.terminal = None
        self.rule = []
        self.start_symbol = None

    def set_non_terminal(self, root):
        self.non_terminal = []
        for i in root[1]:
            self.non_terminal.append(i.attrib['name'])

    def set_terminal(self, root):
        self.terminal = []
        for i in root[0]:
            self.terminal.append(i.attrib['name'])

    def set_production_rules(self, root):
        for elem in root[2]:
            left_side = elem[0].attrib['name']
            right_side = []

            for subElem in elem[1]:
                right_side.append(subElem.attrib['name'])

            trans = Transition(left_side, right_side)
            self.rule.append(trans)

    def set_start_symbol(self, root):
        self.start_symbol = root[3].attrib['name']

    def get_start_symbol(self):
        return self.start_symbol

    def setting(self, root):
        self.set_terminal(root)
        self.set_non_terminal(root)
        self.set_start_symbol(root)
        self.set_production_rules(root)

    def display(self):
        print('-- Non-terminal symbols: ' + str(len(self.non_terminal)))
        for i in range(len(self.non_terminal)):
            print(self.non_terminal[i])
        print()

        print('-- Terminal symbols: ' + str(len(self.terminal)))
        for i in range(len(self.terminal)):
            print(self.terminal[i])
        print()

        print('-- Production rules: ' + str(len(self.rule)))
        for i in range(len(self.rule)):
            print(str(self.rule[i].left_side) + ' ------> ' + str(self.rule[i].right_side))
        print()

        print('-- Start symbol:')
        print(self.start_symbol)
        print()

    def add_production_rules(self, left_side, right_side):
        trans = Transition(left_side, right_side)
        self.rule.append(trans)

    def add_non_terminal(self, symbol):
        self.non_terminal.append(symbol)

    def update_start_symbol(self, symbol):
        self.start_symbol = symbol

    # for remove null
    def remove_production_rule_by_e(self):
        self.rule = [ele for ele in self.rule if ele.right_side != ['e']]

    def remove_terminal_e(self):
        self.terminal.remove('e')

    # for remove unit
    def remove_production_rule_by_unit(self, symbol):
        self.rule = [ele for ele in self.rule if ele.right_side != list(symbol)]

    # for remove useless symbol
    def remove_production_rule_by_useless(self, symbol):
        self.rule = [ele for ele in self.rule if symbol not in ele.right_side]

    def remove_production_rule_by_useless_list(self, x):
        self.rule = [ele for ele in self.rule if ele.left_side not in x]

    def remove_terminal_useless(self, symbol):
        self.non_terminal.remove(symbol)
