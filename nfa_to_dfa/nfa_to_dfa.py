from regex_to_nfas.nfa import NFA
import tools.function as function


class NFAToDFA:
    """Transform NFA to DFA"""

    def __init__(self, nfa, epsilon_closures):
        self.nfa = nfa
        self.epsilon_closures = epsilon_closures
        self.operands = []

    def transform(self):
        tmp = NFA()
        final_state = []
        vertex_from = []
        stored_state = []

        len_final_state = len(self.nfa.get_final_state())
        for i in range(self.nfa.get_final_state()[len_final_state - 1] + 1):
            temp = []
            temp.append(i)
            vertex_from.append(temp)

        while len(vertex_from) > 0:
            tmp_vertex = vertex_from.pop(0)
            stored_state.append(tmp_vertex)

            for operator in range(len(self.epsilon_closures.get_operators())):
                trans_symbol = self.epsilon_closures.get_operators()[operator]

                list_vertex_to = []
                for i in range(len(tmp_vertex)):
                    function.unionList(list_vertex_to, self.nfa.get_list_vertex_to(tmp_vertex[i], trans_symbol))

                if len(list_vertex_to) > 0:
                    tmp.set_transition(tmp_vertex, list_vertex_to, trans_symbol)

                    for i in range(len_final_state):
                        if self.nfa.get_final_state()[i] in list_vertex_to and list_vertex_to not in final_state:
                            final_state.append(list_vertex_to)

                if len(list_vertex_to) > 0 and list_vertex_to not in vertex_from and list_vertex_to not in stored_state:
                    vertex_from.append(list_vertex_to)

        tmp.set_final_state(final_state)

        self.operands.append(tmp)

    def get_transform(self):
        return self.operands[len(self.operands) - 1]
