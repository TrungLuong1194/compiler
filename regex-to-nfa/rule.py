from nfa import NFA

def concat(nfa1, nfa2):
	"""concatenation expression (a.b)"""
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
	"""Kleene star expression (a*)"""
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
	"""union expression (a|b)"""
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
		nfa1.get_vertex_count() + 1,
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