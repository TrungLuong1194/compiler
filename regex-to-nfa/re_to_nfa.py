from nfa import NFA

def concat(nfa1, nfa2):
	result = NFA()

	result.set_vertex(nfa1.get_vertex_count() + nfa2.get_vertex_count())

	for i in range(len(nfa1.transitions)):
		result.set_transition(
			nfa1.transitions[i].vertex_from, 
			nfa1.transitions[i].vertex_to,
			nfa1.transitions[i].trans_symbol)

	result.set_transition(
		nfa1.get_final_state(), 
		nfa1.get_vertex_count(), 
		'eps')

	for i in range(len(nfa2.transitions)):
		result.set_transition(
			nfa2.transitions[i].vertex_from + nfa1.get_vertex_count(), 
			nfa2.transitions[i].vertex_to + nfa1.get_vertex_count(), 
			nfa2.transitions[i].trans_symbol)

	result.set_final_state(nfa1.get_vertex_count() + nfa2.get_vertex_count() - 1)

	return result

def kleene(nfa):
	result = NFA()

	result.set_vertex(nfa.get_vertex_count() + 2)

	result.set_transition(0, 1, 'eps')

	for i in range(len(nfa.transitions)):
		result.set_transition(
			nfa.transitions[i].vertex_from + 1, 
			nfa.transitions[i].vertex_to + 1, 
			nfa.transitions[i].trans_symbol)

	result.set_transition(
		nfa.get_vertex_count(), 
		nfa.get_vertex_count() + 1, 
		'eps')
	result.set_transition(nfa.get_vertex_count(), 1, 'eps')
	result.set_transition(0, nfa.get_vertex_count() + 1, 'eps')

	result.set_final_state(nfa.get_vertex_count() + 1)

	return result

def union(nfa1, nfa2):
	result = NFA()
	
	result.set_vertex(nfa1.get_vertex_count() + nfa2.get_vertex_count() + 2)

	result.set_transition(0, 1, 'eps')

	for i in range(len(nfa1.transitions)):
		result.set_transition(
			nfa1.transitions[i].vertex_from + 1, 
			nfa1.transitions[i].vertex_to + 1, 
			nfa1.transitions[i].trans_symbol)

	result.set_transition(
		nfa1.get_final_state() + 1, 
		nfa1.get_vertex_count() + nfa2.get_vertex_count() + 1, 
		'eps')

	result.set_transition(
		0, 
		nfa2.transitions[i].vertex_from + nfa1.get_vertex_count() + 1, 
		'eps')

	for i in range(len(nfa2.transitions)):
		result.set_transition(
			nfa2.transitions[i].vertex_from + nfa1.get_vertex_count() + 1, 
			nfa2.transitions[i].vertex_to + nfa1.get_vertex_count() + 1, 
			nfa2.transitions[i].trans_symbol)

	result.set_transition(
		nfa2.transitions[i].vertex_to + nfa1.get_vertex_count() + 1, 
		nfa1.get_vertex_count() + nfa2.get_vertex_count() + 1, 
		'eps')

	result.set_final_state(nfa1.get_vertex_count() + nfa2.get_vertex_count() + 1)

	return result

def re_to_nfa(regex):
	operators = []
	operands = []

	for i in range(len(regex)):
		if regex[i] == '*':
			star = operands.pop()
			operands.append(kleene(star))
		elif regex[i] == '.':
			operators.append(regex[i])
		elif regex[i] == '|':
			operators.append(regex[i])
		elif regex[i] == '(':
			operators.append(regex[i])
		elif regex[i] == ')':
			op_count = 0
			op_last = operators[len(operators) - 1]

			while operators[len(operators) - 1] != '(':
				operators.pop()
				op_count += 1
			operators.pop()

			if op_last == '.':
				for i in range(op_count):
					op2 = operands.pop()
					op1 = operands.pop()
					operands.append(concat(op1, op2))
			else:
				for i in range(op_count):
					op2 = operands.pop()
					op1 = operands.pop()
					operands.append(union(op1, op2))
		else:
			tmp = NFA()
			tmp.set_vertex(2)
			tmp.set_transition(0, 1, regex[i])
			tmp.set_final_state(1)
			operands.append(tmp)

	return operands[len(operands) - 1]

#----------------------------------------------------------
print("Thompson's Algorithm")
print('This is a method of transforming a regular expression'
	' into an equivalent nondeterministic finite automaton (NFA)\n')

print('Some examples:\n')

a = NFA()
b = NFA()

a.set_vertex(2)
a.set_transition(0, 1, 'a')
a.set_final_state(1)

b.set_vertex(2)
b.set_transition(0, 1, 'b')
b.set_final_state(1)

print('Regular expression segment: a*')
kleene(a).display()

print('----------------------------------------------------\n')

print('Regular expression segment: (a.b)')
concat(a, b).display()

print('----------------------------------------------------\n')

print('Regular expression segment: (a|b)')
union(a, b).display()

print('----------------------------------------------------\n')

print('Regular expression segment: (a.(b|c))')
re_to_nfa('(a.(b|c))').display()

while True:
	regex = input("Enter a regression (input 'q' to exit): ")
	if regex == 'q':
		break

	print('----------------------------------------------------\n')
	print('The required NFA has the transitions:')
	re_to_nfa(regex).display()