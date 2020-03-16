from nfa import NFA
import function

class NFA_To_DFA:
	"""Transform NFA to DFA"""
	def __init__(self, nfa, epsilonClosures):
		self.nfa = nfa
		self.epsilonClosures = epsilonClosures
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

			for oper in range(len(self.epsilonClosures.getOperators())):
				trans_symbol = self.epsilonClosures.getOperators()[oper]

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

	def get_tranform(self):
		return self.operands[len(self.operands) - 1]


