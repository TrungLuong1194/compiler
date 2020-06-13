from lexer_analysis.regex_to_dfa import RegexToDFA
import string


def isKeyword(word):
    keyword = [
        'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'False',
        'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'None', 'nonlacal', 'not',
        'or', 'pass', 'print', 'range', 'raise', 'return', 'True', 'try', 'while', 'with', 'yield'
    ]

    if word in keyword:
        return True
    else:
        return False


# def isRelativeOperator(word):
#     relOp = '(>|<|=|(>.=)|(<.=)|(=.=)|(=.=.=))'
#
#     operator_token = RegexToDFA(relOp)
#     trans = operator_token.transform()
#     # trans.display()
#
#     current_state = [0]
#
#     for ele in word:
#         flag = False
#         for i in trans.transitions:
#             if current_state == i.vertex_from and ele == i.trans_symbol:
#                 flag = True
#                 current_state = i.vertex_to
#                 break
#
#         if not flag:
#             return False
#
#     if current_state in trans.get_final_state():
#         return True
#     else:
#         return False


def isDelimiter(word):
    delimiter = ['"', ' ', ';', ':', '(', ')', '\n']

    if word in delimiter:
        return True
    else:
        return False


def isOperator(word):
    operator = ['+', '-', '*', '/', '+=', '-=', '/=', '*=', '//', '**', '>', '<', '=', '>=', '<=', '==', '===']

    if word in operator:
        return True
    else:
        return False


def isDigit(word):
    digit = '((0|1|2|3|4|5|6|7|8|9)*)'

    digit_token = RegexToDFA(digit)
    trans = digit_token.transform()
    # trans.display()

    current_state = [0]

    for ele in word:
        flag = False
        for i in trans.transitions:
            if current_state == i.vertex_from and ele == i.trans_symbol:
                flag = True
                current_state = i.vertex_to
                break

        if not flag:
            return False

    if current_state in trans.get_final_state():
        return True
    else:
        return False


def isIdentifier(word):
    letter = string.ascii_letters
    digit = '0123456789'
    test = letter + digit + '_'

    if (word[0] not in letter and word[0] != '_') or word[0] in digit:
        return False
    else:
        for i in range(1, len(word)):
            if word[i] not in test:
                return False

    return True
