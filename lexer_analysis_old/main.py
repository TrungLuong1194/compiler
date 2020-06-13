import lexer_analysis.check_word as check

file = open('input.py', 'r')

word_dict = {}
line_index = 0

for line in file:
    line_index += 1
    word_list = []

    if line != '\n':
        beginPtr = None

        for i in range(len(line)):
            if line[i] != ' ':
                beginPtr = i
                break

        lastPtr = beginPtr

        while lastPtr < len(line):
            if check.isDelimiter(line[lastPtr]):

                if beginPtr != lastPtr:
                    word_list.append(line[beginPtr:lastPtr])
                if line[lastPtr] != ' ' and line[lastPtr] != '\n':
                    word_list.append(line[lastPtr])

                beginPtr = lastPtr + 1

            lastPtr += 1

    word_dict[line_index] = word_list

tokens = {}
index_identifier = 0
index_digit = 0

for key, value in word_dict.items():
    token_list = []
    for v in value:
        if check.isKeyword(v):
            token_list.append('KEYWORD')
        elif check.isDelimiter(v):
            token_list.append(v)
        elif check.isOperator(v):
            token_list.append(v)
        elif check.isDigit(v):
            token_list.append('DIGIT' + str(index_digit))
            index_digit += 1
        elif check.isIdentifier(v):
            token_list.append('ID' + str(index_identifier))
            index_identifier += 1
        else:
            token_list.append('error')

    tokens[key] = token_list

for key, value in tokens.items():
    print(value)





