class Follow:
    """
    Follow Set in Syntax Analysis
    """

    def __init__(self, grammar, first_set):
        self.grammar = grammar
        self.first_set = first_set

    def transform(self):
        # For the start symbol S, place $ in Follow(S)
        follow_dict = {self.grammar.get_start_symbol(): ['$']}

        flag = True
        while flag:
            flag = False
            for i in range(len(self.grammar.rule)):

                # For any production rule A → αB, Follow(B) = Follow(A)
                if self.grammar.rule[i].right_side[-1] in self.grammar.non_terminal:
                    if self.grammar.rule[i].left_side not in follow_dict:
                        pass
                    else:
                        if self.grammar.rule[i].right_side[-1] not in follow_dict:
                            tmp = [ele for ele in follow_dict[self.grammar.rule[i].left_side]]
                            follow_dict[self.grammar.rule[i].right_side[-1]] = tmp
                            flag = True
                        else:
                            for ele in follow_dict[self.grammar.rule[i].left_side]:
                                if ele not in follow_dict[self.grammar.rule[i].right_side[-1]]:
                                    follow_dict[self.grammar.rule[i].right_side[-1]].append(ele)
                                    flag = True

                # For any production rule A → αBβ,
                # If ∈ ∉ First(β), then Follow(B) = First(β)
                # If ∈ ∈ First(β), then Follow(B) = { First(β) – ∈ } ∪ Follow(A)
                count = 0
                while count < len(self.grammar.rule[i].right_side) - 1:
                    if self.grammar.rule[i].right_side[count] in self.grammar.non_terminal:
                        tmp = []
                        for j in range(count + 1, len(self.grammar.rule[i].right_side)):
                            if self.grammar.rule[i].right_side[j] in self.grammar.terminal:
                                tmp.append(self.grammar.rule[i].right_side[j])
                                break
                            else:
                                if 'e' not in self.first_set[self.grammar.rule[i].right_side[j]]:
                                    tmp.append(self.first_set[self.grammar.rule[i].right_side[j]])
                                    break
                                else:
                                    for ele in self.first_set[self.grammar.rule[i].right_side[j]]:
                                        if ele not in tmp:
                                            tmp.append(ele)

                        if 'e' not in tmp:
                            if self.grammar.rule[i].right_side[count] not in follow_dict:
                                follow_dict[self.grammar.rule[i].right_side[count]] = tmp
                                flag = True
                            else:
                                for ele in tmp:
                                    if ele not in follow_dict[self.grammar.rule[i].right_side[count]]:
                                        follow_dict[self.grammar.rule[i].right_side[count]].append(ele)
                                        flag = True
                        else:
                            tmp.remove('e')
                            if self.grammar.rule[i].left_side not in follow_dict:
                                pass
                            else:
                                tmp = list(set().union(tmp, follow_dict[self.grammar.rule[i].left_side]))
                                if self.grammar.rule[i].right_side[count] not in follow_dict:
                                    follow_dict[self.grammar.rule[i].right_side[count]] = tmp
                                    flag = True
                                else:
                                    for ele in tmp:
                                        if ele not in follow_dict[self.grammar.rule[i].right_side[count]]:
                                            follow_dict[self.grammar.rule[i].right_side[count]].append(ele)
                                            flag = True

                    count += 1

        return follow_dict
