class Token:
    def __init__(self):
        self.typeToken = None
        self.value = None
        self.line = None
        self.column = None

    def initValue(self, typeToken, value, line, column):
        self.typeToken = typeToken
        self.value = value
        self.line = line
        self.column = column

    def display(self):
        if self.value:
            print('<' + str(self.typeToken) + ', ' + str(self.value) + ', ' + str(self.line) + ':' +
                  str(self.column) + '>')
        else:
            print('<' + str(self.typeToken) + '>')
