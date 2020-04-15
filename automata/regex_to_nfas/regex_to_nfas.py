from automata.transitions.transitions_setting import TransitionsSetting
import automata.transitions.rule as rule


class RegexToNFAs:
    """
    Transforming a regular expression into an
    equivalent nondeterministic finite automaton - with epsilon (NFAs)
    """

    def __init__(self, regex):
        self.regex = regex
        self.operands = []

    def transform(self):
        operators = []

        for i in range(len(self.regex)):
            if self.regex[i] == '*':
                star = self.operands.pop()
                self.operands.append(rule.kleene(star))
            elif self.regex[i] == '.':
                operators.append(self.regex[i])
            elif self.regex[i] == '|':
                operators.append(self.regex[i])
            elif self.regex[i] == '(':
                operators.append(self.regex[i])
            elif self.regex[i] == ')':
                op_count = 0
                op_last = operators[len(operators) - 1]

                while operators[len(operators) - 1] != '(':
                    operators.pop()
                    op_count += 1
                operators.pop()

                if op_last == '.':
                    for j in range(op_count):
                        op2 = self.operands.pop()
                        op1 = self.operands.pop()
                        self.operands.append(rule.concat(op1, op2))
                else:
                    selections = [0] * (op_count + 1)
                    tracker = op_count
                    for j in range(op_count + 1):
                        selections[tracker] = self.operands.pop()
                        tracker -= 1
                    self.operands.append(rule.union(selections, op_count + 1))

            else:
                tmp = TransitionsSetting()
                tmp.set_vertex(2)
                tmp.set_transition(0, 1, self.regex[i])
                tmp.set_final_state(1)
                self.operands.append(tmp)

    def get_transform(self):
        return self.operands[len(self.operands) - 1]
