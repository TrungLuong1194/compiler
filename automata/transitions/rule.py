from automata.transitions.transitions_setting import TransitionsSetting


def concat(nfa1, nfa2):
    """concatenation expression (a.b)"""
    result = TransitionsSetting()

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
    result = TransitionsSetting()

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


def union(selections, no_of_selections):
    """union expression (a|b)"""
    result = TransitionsSetting()
    vertex_count = 2

    for i in range(no_of_selections):
        vertex_count += selections[i].get_vertex_count()

    result.set_vertex(vertex_count)

    adder_track = 1

    for i in range(no_of_selections):
        result.set_transition(0, adder_track, 'eps')
        med = selections[i]
        for j in range(len(med.transitions)):
            new_trans = med.transitions[j]
            result.set_transition(
                new_trans.vertex_from + adder_track,
                new_trans.vertex_to + adder_track,
                new_trans.trans_symbol)
        adder_track += med.get_vertex_count()

        result.set_transition(adder_track - 1, vertex_count - 1, 'eps')

    result.set_final_state(vertex_count - 1)

    return result
