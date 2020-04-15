from automata.transitions.transitions_setting import TransitionsSetting
import automata.tools.function as function


class NFAsToNFA:
    """Transform NFAs to NFA"""

    def __init__(self, nfas, epsilon_closures):
        self.nfas = nfas
        self.epsilon_closures = epsilon_closures
        self.operands = []

    def transform(self):
        tmp = TransitionsSetting()
        final_state = []

        for operator in range(len(self.nfas.get_operators())):
            trans_symbol = self.nfas.get_operators()[operator]

            for indexStart in range(len(self.epsilon_closures.operands)):
                vertex_from = indexStart
                vertex_to = []

                list_closures = sorted(self.epsilon_closures.operands[indexStart].get_closures())

                if self.nfas.get_final_state() in list_closures and indexStart not in final_state:
                    final_state.append(indexStart)

                list_closures_in = []
                for indexClosure in range(len(list_closures)):
                    if self.nfas.get_vertex_to(list_closures[indexClosure], trans_symbol) != 'empty':
                        list_closures_in.append(self.nfas.get_vertex_to(list_closures[indexClosure], trans_symbol))

                list_tmp = []
                if len(list_closures_in) > 0:
                    for i in range(len(list_closures_in)):
                        list_tmp.append(sorted(self.epsilon_closures.get_epsilon(list_closures_in[i])))

                for i in range(len(list_tmp)):
                    function.union_list(vertex_to, list_tmp[i])

                if len(vertex_to) > 0:
                    for i in range(len(vertex_to)):
                        tmp.set_transition(vertex_from, vertex_to[i], trans_symbol)

        tmp.set_final_state(final_state)

        self.operands.append(tmp)

    def get_transform(self):
        return self.operands[len(self.operands) - 1]
