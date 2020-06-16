class First:
    """
    FIRST Set in Syntax Analysis
    """

    def __init__(self, grammar):
        self.grammar = grammar

    def transform(self):
        first_dict = {}

        flag = True
        while flag:
            flag = False

            for i in range(len(self.grammar.rule)):

                # For a production rule X -> e, First(X) = ['e']
                if self.grammar.rule[i].right_side[0] == ['e']:
                    if self.grammar.rule[i].left_side in first_dict:
                        first_dict[self.grammar.rule[i].left_side].append('e')
                        flag = True
                    else:
                        first_dict[self.grammar.rule[i].left_side] = ['e']
                        flag = True

                # For a production rule X -> aA.., First(X) = ['a']
                if self.grammar.rule[i].right_side[0] in self.grammar.terminal:
                    if self.grammar.rule[i].left_side in first_dict and \
                            self.grammar.rule[i].right_side[0] not in first_dict[self.grammar.rule[i].left_side]:
                        first_dict[self.grammar.rule[i].left_side].append(self.grammar.rule[i].right_side[0])
                        flag = True

                    if self.grammar.rule[i].left_side not in first_dict:
                        first_dict[self.grammar.rule[i].left_side] = [self.grammar.rule[i].right_side[0]]
                        flag = True

                # For a production rule X -> Y0 Y1 Y2
                # If e ∉ First(Y0), then First(X) = First(Y0)
                # If e ∈ First(Y0), then First(X) = [ First(Y0) – e ] ∪ First(Y1 Y2)
                if self.grammar.rule[i].right_side[0] in self.grammar.non_terminal:
                    check = True

                    for ele in self.grammar.rule[i].right_side:
                        if ele in self.grammar.non_terminal and ele not in first_dict:
                            check = False

                    if not check:
                        pass
                    else:
                        count = 0
                        tmp = []
                        while count < len(self.grammar.rule[i].right_side):
                            if self.grammar.rule[i].right_side[count] in self.grammar.terminal:
                                tmp.append(self.grammar.rule[i].right_side[count])
                                break
                            else:
                                if 'e' not in first_dict[self.grammar.rule[i].right_side[count]]:
                                    for ele in first_dict[self.grammar.rule[i].right_side[count]]:
                                        if ele not in tmp:
                                            tmp.append(ele)
                                    break
                                else:
                                    for ele in first_dict[self.grammar.rule[i].right_side[count]]:
                                        if ele not in tmp:
                                            tmp.append(ele)

                            count += 1

                        if self.grammar.rule[i].left_side in first_dict:
                            for ele in tmp:
                                if ele not in first_dict[self.grammar.rule[i].left_side]:
                                    first_dict[self.grammar.rule[i].left_side].append(ele)
                                    flag = True
                        else:
                            first_dict[self.grammar.rule[i].left_side] = tmp
                            flag = True

        return first_dict
