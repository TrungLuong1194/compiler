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

        flag = True

        tokens_list.append('$')

        stack = ['$', self.grammar.get_start_symbol()]

        print('\n')
        print('-- tokens_list:')
        print(tokens_list)
        print('\n')
        # print(stack)
        print('-- Parser tree:')

        index = 0

        while len(stack) > 0:
            top = stack[len(stack) - 1]

            print('-' * 20)
            print('Top --> ' + str(top))

            current_token = tokens_list[index]

            print('Current_token --> ' + str(current_token))

            if top == current_token:
                stack.pop()
                index += 1
            else:
                key = (top, current_token)
                print(key)

                if key not in self.parse_table:
                    flag = False
                    break

                value = self.grammar.rule[self.parse_table[key] - 1].right_side
                if value != ['e']:
                    value = value[::-1]

                    stack.pop()

                    for ele in value:
                        stack.append(ele)
                else:
                    stack.pop()

        if flag:
            print('Token accepted!')
        else:
            print('Token not accepted!')
