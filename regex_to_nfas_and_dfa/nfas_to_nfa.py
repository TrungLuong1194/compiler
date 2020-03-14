import function
from nfa import NFA

class NFAs_To_NFA:
	"""Transform NFAs to NFA"""
	def __init__(self, epsilonClosures, nfa):
		self.epsilonClosures = epsilonClosures
		self.nfa = nfa
		self.operands = []

	def transform(self):
		tmp = NFA()
		tmp.set_vertex(2 * len(self.epsilonClosures.operands))
		final_state = []
		
		for oper in range(len(self.epsilonClosures.getOperators())):
			trans_symbol = self.epsilonClosures.getOperators()[oper]

			for indexStart in range(len(self.epsilonClosures.operands)):
				vertex_from = indexStart
				vertex_to = []
				
				listClosures = sorted(self.epsilonClosures.operands[indexStart].getClosure())

				if self.nfa.get_final_state() in listClosures and indexStart not in final_state:
					final_state.append(indexStart)

				listClosuresIn = []
				for indexClosure in range(len(listClosures)):
					if self.nfa.get_vertex_to(listClosures[indexClosure], trans_symbol) != 'empty':
						listClosuresIn.append(self.nfa.get_vertex_to(listClosures[indexClosure], trans_symbol))

				listTmp = []
				if len(listClosuresIn) > 0:
					for i in range(len(listClosuresIn)):
						listTmp.append(sorted(self.epsilonClosures.get_epsilon(listClosuresIn[i])))

				for i in range(len(listTmp)):
					function.unionList(vertex_to, listTmp[i])

				if len(vertex_to) > 0:
					for i in range(len(vertex_to)):
						tmp.set_transition(vertex_from, vertex_to[i], trans_symbol)

		tmp.set_final_state(final_state)

		self.operands.append(tmp)

	def get_tranform(self):
		return self.operands[len(self.operands) - 1]