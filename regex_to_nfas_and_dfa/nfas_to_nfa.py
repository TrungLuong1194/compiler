import function
from nfa import NFA
from re_to_nfas import Re_To_NFAs
from epsilon_closures import EpsilonClosures

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

				listClosuresIn = []
				for indexClosure in range(len(listClosures)):
					if self.nfa.get_vertex_to(listClosures[indexClosure], trans_symbol) != 'O':
						listClosuresIn.append(self.nfa.get_vertex_to(listClosures[indexClosure], trans_symbol))

				listTmp = []
				if len(listClosuresIn) > 0:
					for i in range(len(listClosuresIn)):
						listTmp.append(sorted(self.epsilonClosures.get_epsilon(listClosuresIn[i])))

				for i in range(len(listTmp)):
					function.unionList(vertex_to, listTmp[i])

				tmp.set_transition(vertex_from, vertex_to, trans_symbol)

		self.operands.append(tmp)

	def get_tranform(self):
		return self.operands[len(self.operands) - 1]




# regex = '((a*|b).c*)'
regex = '(a*|b)'
regex_tranform = Re_To_NFAs(regex)
regex_tranform.matcher()
nfa = regex_tranform.get_tranform()

# print(len(nfa.transitions))

# print(regex_tranform.get_tranform().transitions[4].trans_symbol)

eli = EpsilonClosures(nfa)
eli.transform()
eli.optimize()
for i in range(len(eli.operands)):
	eli.operands[i].display()

print('--------------------------------')






nfas = NFAs_To_NFA(eli, nfa)
nfas.transform()
nfas.get_tranform().display()
					
