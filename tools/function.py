def concatList(listA, listB):
    if listB[0] in listA:
        for i in range(1, len(listB)):
            if listB[i] not in listA:
                listA.append(listB[i])

    return listA


def unionList(listA, listB):
    for i in range(len(listB)):
        if listB[i] not in listA:
            listA.append(listB[i])

    return listA
