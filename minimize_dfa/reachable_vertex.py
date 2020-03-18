from transitions.initial_transitions import InitialTransitions
import tools.function as function


def find_next_vertex(index, tmp, initial_transitions, trans_symbol):
    for i in range(len(tmp.transitions)):
        if tmp.transitions[i].vertex_from == index and tmp.transitions[i].trans_symbol == trans_symbol \
                and tmp.transitions[i].vertex_to not in initial_transitions.get_transitions():
            initial_transitions.add_value(tmp.transitions[i].vertex_to)


class ReachableVertex:
    """Find out all vertexes from the initial state"""

    def __init__(self, dfa):
        self.dfa = dfa
        self.operands = []

    def transform(self):
        list_vertex_from = []
        for i in range(len(self.dfa.transitions)):
            if self.dfa.transitions[i].vertex_from not in list_vertex_from:
                list_vertex_from.append(self.dfa.transitions[i].vertex_from)

        for i in range(len(list_vertex_from)):
            initial_transitions = InitialTransitions(list_vertex_from[i])
            initial_transitions.add_value(list_vertex_from[i])
            for operator in range(len(self.dfa.get_operators())):
                trans_symbol = self.dfa.get_operators()[operator]
                find_next_vertex(list_vertex_from[i], self.dfa, initial_transitions, trans_symbol)

            self.operands.append(initial_transitions)

        for i in range(len(list_vertex_from)):
            for j in range(i + 1, len(list_vertex_from)):
                function.concat_list(self.operands[i].get_transitions(), self.operands[j].get_transitions())

    def get_reachable_vertex(self):
        return self.operands[0].get_transitions()
