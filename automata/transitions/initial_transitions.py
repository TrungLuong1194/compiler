class InitialTransitions:
    """The grammar_settings from the initial state"""

    def __init__(self, start):
        self.start = start
        self.transitions = []

    def add_value(self, value):
        self.transitions.append(value)

    def get_transitions(self):
        return self.transitions
