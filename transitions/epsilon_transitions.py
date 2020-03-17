class EpsilonTransitions:
    """Find out all the ε transitions from each state"""

    def __init__(self, start):
        self.start = start
        self.closures = []

    def add_value(self, value):
        self.closures.append(value)

    def get_closures(self):
        return self.closures
