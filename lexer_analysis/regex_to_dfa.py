from automata.regex_to_nfas.regex_to_nfas import RegexToNFAs
from automata.nfas_to_nfa.epsilon_closures import EpsilonClosures
from automata.nfas_to_nfa.nfas_to_nfa import NFAsToNFA
from automata.nfa_to_dfa.nfa_to_dfa import NFAToDFA
from automata.minimize_dfa.reachable_vertex import ReachableVertex
from automata.minimize_dfa.minimize_dfa import MinimizeDFA


class RegexToDFA:
    def __init__(self, regex):
        self.regex = regex

    def transform(self):
        regex_to_nfas = RegexToNFAs(self.regex)
        regex_to_nfas.transform()
        regex_to_nfas.get_transform().display()

        nfas = regex_to_nfas.get_transform()
        eps = EpsilonClosures(nfas)
        eps.transform()

        nfas_to_nfa = NFAsToNFA(nfas, eps)
        nfas_to_nfa.transform()
        nfas_to_nfa.get_transform().display()

        nfa = nfas_to_nfa.get_transform()
        nfa_to_dfa = NFAToDFA(nfa)
        nfa_to_dfa.transform()
        nfa_to_dfa.get_transform().display()

        dfa = nfa_to_dfa.get_transform()
        reachable_vertex = ReachableVertex(dfa)
        reachable_vertex.transform()

        minimize_dfa = MinimizeDFA(dfa, reachable_vertex)
        minimize_dfa.transform()
        minimize_dfa.get_transform().display()

        # return minimize_dfa.get_transform()
