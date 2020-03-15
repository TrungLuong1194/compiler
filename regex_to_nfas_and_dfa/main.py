from nfa import NFA
from re_to_nfas import Re_To_NFAs
from epsilon_closures import EpsilonClosures
from nfas_to_nfa import NFAs_To_NFA
from nfa_to_dfa import NFA_To_DFA
import rule

# print("Thompson's Algorithm")
# print('This is a method of transforming a regular expression'
# 	' into an equivalent nondeterministic finite automaton (NFA)\n')

# print('Some examples:\n')

# a = NFA()
# b = NFA()

# a.set_vertex(2)
# a.set_transition(0, 1, 'a')
# a.set_final_state(1)

# b.set_vertex(2)
# b.set_transition(0, 1, 'b')
# b.set_final_state(1)

# print('Regular expression segment: a*')
# rule.kleene(a).display()

# print('----------------------------------------------------\n')

# print('Regular expression segment: (a.b)')
# rule.concat(a, b).display()

# print('----------------------------------------------------\n')

# no_of_selections = 2
# selections = []
# selections.append(a)
# selections.append(b)
# print('Regular expression segment: (a|b)')
# rule.union(selections, no_of_selections).display()

# print('----------------------------------------------------\n')

# print('Regular expression segment: (a.(b|c))')
# regex = '(a.(b|c))'
# regex_tranform = Re_To_NFAs(regex)
# regex_tranform.matcher()
# regex_tranform.get_tranform().display()

while True:
	regex = input("Enter a regression (input 'q' to exit): ")
	if regex == 'q':
		break

	print('\nThe required NFAs (with epsilon) has the transitions:\n')
	regex_tranform = Re_To_NFAs(regex)
	regex_tranform.matcher()
	regex_tranform.get_tranform().display()

	print('----------------------------------------------------\n')

	print('The required NFA (without epsilon) has the transitions:\n')
	nfas = regex_tranform.get_tranform()
	eps = EpsilonClosures(nfas)
	eps.transform()
	eps.optimize()

	nfas_tranform = NFAs_To_NFA(eps, nfas)
	nfas_tranform.transform()
	nfas_tranform.get_tranform().display()

	print('----------------------------------------------------\n')

	print('The required DFA has the transitions:\n')

	nfa = nfas_tranform.get_tranform()
	nfa_tranform = NFA_To_DFA(nfa, eps)
	nfa_tranform.transform()
	nfa_tranform.get_tranform().display()
