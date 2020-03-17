def concat_list(list1, list2):
    if list2[0] in list1:
        for i in range(1, len(list2)):
            if list2[i] not in list1:
                list1.append(list2[i])

    return list1


def union_list(list1, list2):
    for i in range(len(list2)):
        if list2[i] not in list1:
            list1.append(list2[i])

    return list1
