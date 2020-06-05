import itertools


def intersection(lst1, lst2):
    """intersection of two lists"""
    return list(set(lst1) & set(lst2))


def combinations_list(x):
    """
    combination a list
    Ex: x = [0, 1, 2]
    return [[0], [1], [2], [0, 1], [0, 2], [1, 2], [0, 1, 2]]
    """
    x_new = []
    for i in range(len(x)):
        for j in itertools.combinations(x, i + 1):
            x_new.append(list(j))

    return x_new


def remove_list(x, index):
    """
    remove a list with index
    Ex: x = ['A', 'B', 'C'], index = [[0], [1, 2]]
    return [['B', 'C'], ['A']]
    """
    x_new = []
    for i in range(len(index)):
        x_new.append([v for k, v in enumerate(x) if k not in index[i]])

    return x_new
