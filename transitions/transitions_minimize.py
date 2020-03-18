from transitions.transition import Transition


class TransitionsMinimize:
    """Setting a transition minimize"""

    def __init__(self):
        self.transitions = []

    def set_transition(self, vertex_from, vertex_to, trans_symbol):
        trans = Transition(vertex_from, vertex_to, trans_symbol)
        self.transitions.append(trans)

    def remove_duplicate(self):
        transitions_no_duplicate = []

        for i in range(len(self.transitions)):
            is_duplicate = False
            if len(transitions_no_duplicate) == 0:
                transitions_no_duplicate.append(self.transitions[i])
            else:
                index = 0
                while index < len(transitions_no_duplicate):
                    if self.transitions[i].trans_symbol == transitions_no_duplicate[index].trans_symbol and \
                            self.transitions[i].vertex_to == transitions_no_duplicate[index].vertex_to:
                        is_duplicate = True

                        for j in range(len(transitions_no_duplicate)):
                            if transitions_no_duplicate[j].vertex_to == self.transitions[i].vertex_from:
                                transitions_no_duplicate[j].vertex_to = transitions_no_duplicate[index].vertex_from
                        break
                    else:
                        index += 1

                if not is_duplicate:
                    transitions_no_duplicate.append(self.transitions[i])

        self.transitions = transitions_no_duplicate

    def display(self):
        for i in range(len(self.transitions)):
            print('q' + str(self.transitions[i].vertex_from) + '------ ' + self.transitions[
                i].trans_symbol + ' ------> q' + str(self.transitions[i].vertex_to))
