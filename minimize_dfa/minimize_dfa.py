class MinimizeDFA:
    """Minimization of DFA means reducing the number of states from given FA"""

    def __init__(self, nfa, epsilon_closures):
        self.nfa = nfa
        self.epsilon_closures = epsilon_closures
        self.operands = []

    def remove_vertex(self):
        """Remove all the states that are unreachable from the initial state via any set of the transition of DFA"""
        for operator in range(len(self.epsilon_closures.get_operators())):
            trans_symbol = self.epsilon_closures.get_operators()[operator]
            print(trans_symbol)