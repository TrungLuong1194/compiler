from lexer_analysis.util.state import State


class FSM:

    def __init__(self):
        self.states = None
        self.initialState = None
        self.acceptingStates = None
        self.nextState = None

    def run(self, input):
        buffer = ''
        currentState = self.initialState

        for i in range(len(input)):
            character = input[i]

            nextState = self.nextState(currentState, character)

            if nextState == State.NoNextState.value:
                break

            currentState = nextState

            buffer += character

        return currentState in self.acceptingStates, buffer
