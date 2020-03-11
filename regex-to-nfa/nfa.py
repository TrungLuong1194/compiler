from transitions import Transitions

class NFA:
	def __init__(self):
		self.vertex = []
		self.transitions = []
		self.final_state = 0

	def get_vertex_count(self):
		return len(self.vertex)

	def set_vertex(self, no_vertex):
		for i in range(no_vertex):
			self.vertex.append(i)

	def set_transition(self, vertex_from, vertex_to, trans_symbol):
		trans = Transitions(vertex_from, vertex_to, trans_symbol)
		self.transitions.append(trans)

	def set_final_state(self, final_state):
		self.final_state = final_state

	def get_final_state(self):
		return self.final_state

	def display(self):
		for i in range(len(self.transitions)):
			print('q' + str(self.transitions[i].vertex_from) + ' ---> q' + 
				str(self.transitions[i].vertex_to) + ' : Symbol - ' + self.transitions[i].trans_symbol)

		print('\nThe final state is q' + str(self.get_final_state()) + '\n')






# nfa = NFA()
# nfa.set_transition(1, 2, 'e')
# nfa.set_final_state(10)
# nfa.display()
# nfa.set_vertex(3)
# print(nfa.get_vertex_count())
# print(nfa.vertex)