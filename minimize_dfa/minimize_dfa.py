from transitions.transitions_setting import TransitionsSetting
from transitions.transitions_minimize import TransitionsMinimize


class MinimizeDFA:
    """Minimization of DFA means reducing the number of states from given FA"""

    def __init__(self, dfa, reachable_vertex):
        self.dfa = dfa
        self.reachable_vertex = reachable_vertex
        self.operands = []

    def transform(self):
        # One set contains those rows, which start from non-final states
        # The other contains those rows, which start from final states
        non_final = TransitionsMinimize()
        final = TransitionsMinimize()
        for i in range(len(self.dfa.transitions)):
            if self.dfa.transitions[i].vertex_from in self.reachable_vertex.get_reachable_vertex() and \
                    self.dfa.transitions[i].vertex_from not in self.dfa.get_final_state():
                non_final.set_transition(
                    self.dfa.transitions[i].vertex_from,
                    self.dfa.transitions[i].vertex_to,
                    self.dfa.transitions[i].trans_symbol)
            if self.dfa.transitions[i].vertex_from in self.reachable_vertex.get_reachable_vertex() and \
                    self.dfa.transitions[i].vertex_from in self.dfa.get_final_state():
                final.set_transition(
                    self.dfa.transitions[i].vertex_from,
                    self.dfa.transitions[i].vertex_to,
                    self.dfa.transitions[i].trans_symbol)

        # Remove duplicate in sets
        non_final.remove_duplicate()
        final.remove_duplicate()

        # Combined transition
        tmp = TransitionsSetting()
        for i in range(len(non_final.transitions)):
            tmp.set_transition(
                non_final.transitions[i].vertex_from,
                non_final.transitions[i].vertex_to,
                non_final.transitions[i].trans_symbol)

        for i in range(len(final.transitions)):
            tmp.set_transition(
                final.transitions[i].vertex_from,
                final.transitions[i].vertex_to,
                final.transitions[i].trans_symbol)

        tmp.set_final_state(self.dfa.get_final_state())

        self.operands.append(tmp)

    def get_transform(self):
        return self.operands[len(self.operands) - 1]
