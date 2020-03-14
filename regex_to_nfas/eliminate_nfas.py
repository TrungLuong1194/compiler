from transitions_closures import TransitionsClosures as Trans
from re_to_nfa import RE_TO_NFA
import function

class EliminateNFA:
	def __init__(self, nfa):
		self.nfa = nfa
		self.tranforms = []

	def find_epsilon(self, index, tmp, trans):
		for i in range(len(tmp.transitions)):
			if tmp.transitions[i].vertex_from == index and tmp.transitions[i].trans_symbol == 'eps' 
			and tmp.transitions[i].vertex_to not in trans.getClosure():
				trans.addValue(tmp.transitions[i].vertex_to)

	def epsilonClosures(self):
		for i in range(nfa.get_final_state() + 1):
			trans = Trans(i)
			trans.addValue(i)
			self.find_epsilon(i, self.nfa, trans)
			self.tranforms.append(trans)

	def optimized(self):
		for i in range(nfa.get_final_state()):
			for j in range(i + 1, nfa.get_final_state()):
				function.concatList(self.tranforms[i].getClosure(), self.tranforms[j].getClosure())






# regex = '((a*|b).c*)'
regex = '(a*|b)'
regex_tranform = RE_TO_NFA(regex)
regex_tranform.matcher()
nfa = regex_tranform.get_tranform()

print(len(nfa.transitions))

# print(regex_tranform.get_tranform().transitions[4].trans_symbol)

eli = EliminateNFA(nfa)
eli.epsilonClosures()
eli.optimized()
for i in range(len(eli.tranforms)):
	eli.tranforms[i].display()

