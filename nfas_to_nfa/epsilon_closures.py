from nfas_to_nfa.transitions_closures import TransitionsClosures as Trans
import tools.function as function


class EpsilonClosures:
    """Find epsilon-closure of vertexes"""

    def __init__(self, nfa):
        self.nfa = nfa
        self.operands = []
        self.operators = []

    def get_operators(self):
        for i in range(len(self.nfa.transitions)):
            if self.nfa.transitions[i].trans_symbol not in self.operators \
                    and self.nfa.transitions[i].trans_symbol != 'eps':
                self.operators.append(self.nfa.transitions[i].trans_symbol)

        return self.operators

    def find_epsilon(self, index, tmp, trans):
        for i in range(len(tmp.transitions)):
            if tmp.transitions[i].vertex_from == index and tmp.transitions[i].trans_symbol == 'eps' \
                    and tmp.transitions[i].vertex_to not in trans.get_closure():
                trans.add_value(tmp.transitions[i].vertex_to)

    def transform(self):
        for i in range(self.nfa.get_final_state() + 1):
            trans = Trans(i)
            trans.add_value(i)
            self.find_epsilon(i, self.nfa, trans)
            self.operands.append(trans)

    def optimize(self):
        for i in range(self.nfa.get_final_state()):
            for j in range(i + 1, self.nfa.get_final_state()):
                function.concatList(self.operands[i].get_closure(), self.operands[j].get_closure())

    def get_epsilon(self, index):
        return self.operands[index].get_closure()
