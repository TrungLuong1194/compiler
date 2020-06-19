import pandas as pd
import numpy as np
from syntax_analysis.LL1.first import First
from syntax_analysis.LL1.follow import Follow


class ParseTable:
    """
    Create LL(1) parse table
    """

    def __init__(self, grammar):
        self.grammar = grammar

    def transform(self):
        # create first set and follow set
        # first set
        first = First(self.grammar)
        first_set, parse_table = first.transform()

        follow = Follow(self.grammar, first_set)
        follow_set = follow.transform()

        # add 'e' in parse table
        tmp = []
        for i, v in first_set.items():
            if 'e' in v:
                tmp.append(i)

        tmp_dict = {}
        for ele in tmp:
            for i in range(len(self.grammar.rule)):
                if self.grammar.rule[i].left_side == ele and self.grammar.rule[i].right_side == ['e']:
                    tmp_dict[ele] = i + 1
                    break

        for i, v in follow_set.items():
            if i in tmp_dict:
                for ele in v:
                    parse_table[(i, ele)] = tmp_dict[i]

        # # parse table
        # print('-' * 50)
        # print('Parse Table:')
        #
        # for i, v in self.parse_table.items():
        #     print(str(i) + ' - ' + str(v))

        # create table in pandas
        index = []
        columns = []

        for ele in self.grammar.non_terminal:
            index.append(ele)

        for ele in self.grammar.terminal:
            columns.append(ele)

        columns.append('$')

        df = pd.DataFrame(np.zeros((len(index), len(columns)), dtype=int), index=index, columns=columns)

        for i, v in parse_table.items():
            df.loc[i[0], i[1]] = v

        return df, parse_table
