from automata.transitions.transitions_setting import TransitionsSetting


class MinimizeDFA:
    """Minimization of DFA means reducing the number of states from given FA"""

    def __init__(self, dfa, reachable_vertex):
        self.dfa = dfa
        self.reachable_vertex = reachable_vertex
        self.operands = []

    def transform(self):
        tmp = TransitionsSetting()

        for ele in self.dfa.transitions:
            if ele.vertex_from in self.reachable_vertex.get_reachable_vertex():
                tmp.set_transition(ele.vertex_from, ele.vertex_to, ele.trans_symbol)

        final_state = [x for x in self.dfa.get_final_state() if x in self.reachable_vertex.get_reachable_vertex()]

        tmp.set_final_state(final_state)

        self.operands.append(tmp)

    def get_transform(self):
        return self.operands[len(self.operands) - 1]
