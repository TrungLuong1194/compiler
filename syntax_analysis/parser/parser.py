class Parser:
    def __init__(self, grammar, parse_table, tokens):
        self.grammar = grammar
        self.parse_table = parse_table
        self.tokens = tokens

    def transform(self):
        tokens_list = []
        for ele in self.tokens:
            if ele.typeToken not in ['NewLine', 'EndOfInput']:
                tokens_list.append(ele.typeToken)

        print(tokens_list)

        # flag = True
        #
        # token = input + '$'
        #
        # stack = ['$', self.grammar.get_start_symbol()]
        #
        # index = 0
        #
        # while len(stack) > 0:
        #     top = stack[len(stack) - 1]
        #
        #     print('Top --> ' + str(top))
        #
        #     current_token = token[index]
        #
        #     print('Current_token --> ' + str(current_token))
        #
        #     if top == current_token:
        #         stack.pop()
        #         index += 1
        #     else:
        #         key = (top, current_token)
        #         print(key)
        #
        #         if key not in self.parse_table:
        #             flag = False
        #             break
        #
        #         value = self.grammar.rule[self.parse_table[key] - 1].right_side
        #         if value != ['e']:
        #             value = value[::-1]
        #
        #             stack.pop()
        #
        #             for ele in value:
        #                 stack.append(ele)
        #         else:
        #             stack.pop()
        #
        # if flag:
        #     print('Token accepted!')
        # else:
        #     print('Token not accepted!')
