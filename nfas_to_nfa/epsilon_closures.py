from transitions.epsilon_transitions import EpsilonTransitions
import tools.function as function


def find_epsilon(index, tmp, epsilon_transitions):
    for i in range(len(tmp.transitions)):
        if tmp.transitions[i].vertex_from == index and tmp.transitions[i].trans_symbol == 'eps' \
                and tmp.transitions[i].vertex_to not in epsilon_transitions.get_closures():
            epsilon_transitions.add_value(tmp.transitions[i].vertex_to)


class EpsilonClosures:
    """Find epsilon-closures of vertexes"""

    def __init__(self, nfas):
        self.nfas = nfas
        self.operands = []

    def transform(self):
        list_vertex_from = []
        for i in range(self.nfas.get_final_state() + 1):
            list_vertex_from.append(i)

        for i in range(len(list_vertex_from)):
            epsilon_transitions = EpsilonTransitions(list_vertex_from[i])
            epsilon_transitions.add_value(list_vertex_from[i])
            find_epsilon(list_vertex_from[i], self.nfas, epsilon_transitions)
            self.operands.append(epsilon_transitions)

        for i in range(len(list_vertex_from)):
            for j in range(i + 1, len(list_vertex_from)):
                function.concat_list(self.operands[i].get_closures(), self.operands[j].get_closures())

    def get_epsilon(self, index):
        return self.operands[index].get_closures()
