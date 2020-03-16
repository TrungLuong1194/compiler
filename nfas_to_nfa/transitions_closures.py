class TransitionsClosures:
    def __init__(self, start):
        self.start = start
        self.closure = []

    def add_value(self, value):
        self.closure.append(value)

    def get_closure(self):
        return self.closure

    def display(self):
        print('q' + str(self.start) + ' = q' + str(sorted(self.closure)))
