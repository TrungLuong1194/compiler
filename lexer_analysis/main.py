# from lexer_analysis.regex_to_dfa import RegexToDFA
# import string
#
# # Digits
# digit = '(0|1|2|3|4|5|6|7|8|9)'
#
# digit_token = RegexToDFA(digit)
# # digit_token.transform()
#
# trans = digit_token.transform()
# trans.display()
#
#
# # Letters
# letter = string.ascii_letters
# letter_list = '('
#
# for i in letter:
#     letter_list += i
#     if i != 'Z':
#         letter_list += '|'
#
# letter_list = letter_list + ')'
#
# letter_token = RegexToDFA(letter_list)
# letter_token.transform()
#
# # Operators
# operator = '(<|>|=|(<.=)|(>.=)|(=.=))'
#
# operator_token = RegexToDFA(operator)
# operator_token.transform()

from lexer_analysis.check_lexeme import CheckLexeme

check_lexeme = CheckLexeme('1234')
check_lexeme.isdigit()
