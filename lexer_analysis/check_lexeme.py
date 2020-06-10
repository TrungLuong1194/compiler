from lexer_analysis.regex_to_dfa import RegexToDFA


class CheckLexeme:
    def __init__(self, lexeme):
        self.lexeme = lexeme

    def iskeyword(self):
        keyword = [
            'int',
            'float',
            'double'
        ]

        if self.lexeme in keyword:
            return True
        else:
            return False

    def isdigit(self):
        # Digits
        digit = '((0|1|2|3|4|5|6|7|8|9)*)'

        digit_token = RegexToDFA(digit)
        trans = digit_token.transform()
        # trans.display()
        #
        # current_state = 0
        #
        # for index in range(len(self.lexeme)):
        #     print('-' * 40)
        #     print('-' * 40)
        #     print(self.lexeme[index])
        #     print(current_state)
        #     print('-' * 40)
        #
        #     for i in range(len(trans.transitions)):
        #         for j in trans.transitions[i].trans_symbol:
        #             print(j)
        #             if self.lexeme[index] == j:
        #                 print('aaaaaaa')
        #                 current_state = trans.transitions[i].vertex_to
        #             #     break
        #         # break
