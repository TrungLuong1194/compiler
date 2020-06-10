from automata.transitions.transition import Transition


class TransitionsMinimize:
    """Setting a transition minimize"""

    def __init__(self):
        self.transitions = []

    def set_transition(self, vertex_from, vertex_to, trans_symbol):
        trans = Transition(vertex_from, vertex_to, trans_symbol)
        self.transitions.append(trans)

    def remove_duplicate(self):
        transitions_no_duplicate = []
        vertex_from_list = []
        transition_dict = {}

        for ele in self.transitions:
            if ele.vertex_from not in vertex_from_list:
                vertex_from_list.append(ele.vertex_from)
                transition_dict[vertex_from_list.index(ele.vertex_from)] = [[ele.trans_symbol, ele.vertex_to]]
            else:
                transition_dict[vertex_from_list.index(ele.vertex_from)].append([ele.trans_symbol, ele.vertex_to])

        duplicate_dict = {}

        for i1, v1 in transition_dict.items():
            if not duplicate_dict:
                duplicate_dict[i1] = [i1]
            else:
                for i2, v2 in duplicate_dict.items():
                    if v1 == transition_dict[i2]:
                        duplicate_dict[i2].append(i1)

        for i, v in duplicate_dict.items():
            for ele in self.transitions:
                if ele.vertex_from == vertex_from_list[i]:
                    transitions_no_duplicate.append(ele)

        for value in duplicate_dict.values():

            duplicate_result = [vertex_from_list[i] for i in range(len(vertex_from_list)) if i in value]

            for index in range(len(transitions_no_duplicate)):
                if transitions_no_duplicate[index].vertex_from in duplicate_result and \
                        transitions_no_duplicate[index].vertex_from != duplicate_result[0]:
                    transitions_no_duplicate[index].vertex_from = duplicate_result[0]

                if transitions_no_duplicate[index].vertex_to in duplicate_result and \
                        transitions_no_duplicate[index].vertex_to != duplicate_result[0]:
                    transitions_no_duplicate[index].vertex_to = duplicate_result[0]

        self.transitions = transitions_no_duplicate

    def display(self):
        for i in range(len(self.transitions)):
            print('q' + str(self.transitions[i].vertex_from) + '------ ' + self.transitions[
                i].trans_symbol + ' ------> q' + str(self.transitions[i].vertex_to))
