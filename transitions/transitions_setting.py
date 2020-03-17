from transitions.transition import Transition


class TransitionsSetting:
    """Setting a transition model"""

    def __init__(self):
        self.vertex = []
        self.transitions = []
        self.final_state = 0
        self.operators = []

    def get_vertex_count(self):
        return len(self.vertex)

    def set_vertex(self, no_vertex):
        for i in range(no_vertex):
            self.vertex.append(i)

    def set_transition(self, vertex_from, vertex_to, trans_symbol):
        trans = Transition(vertex_from, vertex_to, trans_symbol)
        self.transitions.append(trans)

    def set_final_state(self, final_state):
        self.final_state = final_state

    def get_final_state(self):
        return self.final_state

    def get_operators(self):
        for i in range(len(self.transitions)):
            if self.transitions[i].trans_symbol != 'eps' and self.transitions[i].trans_symbol not in self.operators:
                self.operators.append(self.transitions[i].trans_symbol)

        return self.operators

    def get_vertex_to(self, vertex_from, trans_symbol):
        vertex_to = 'empty'
        for i in range(len(self.transitions)):
            if self.transitions[i].vertex_from == vertex_from and self.transitions[i].trans_symbol == trans_symbol:
                vertex_to = self.transitions[i].vertex_to

        return vertex_to

    def get_list_vertex_to(self, vertex_from, trans_symbol):
        list_vertex_to = []

        for index in range(len(self.transitions)):
            if self.transitions[index].vertex_from == vertex_from and \
                    self.transitions[index].trans_symbol == trans_symbol:
                list_vertex_to.append(self.transitions[index].vertex_to)

        return list_vertex_to

    def display(self):
        for i in range(len(self.transitions)):
            print('q' + str(self.transitions[i].vertex_from) + '------ ' + self.transitions[
                i].trans_symbol + ' ------> q' + str(self.transitions[i].vertex_to))

        print('\nThe final state is q' + str(self.get_final_state()) + '\n')
