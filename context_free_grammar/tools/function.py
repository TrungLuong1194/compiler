import itertools


# def is_child_list(a, b):
#     """
#     Checking elements of list a on list b
#     eg: [x, y] on [x, y, z]
#     """
#     count = 0
#     for i in range(len(a)):
#         if a[i] in b:
#             count += 1
#
#     if count == len(a):
#         return True
#
#     return False
#
#
# def remove_string_by_index(string, tup):
#     """Remove multiple characters of string by index. Indexes are determined in tuple"""
#     for i in range(len(tup)):
#         string = string[0:tup[i] - i:] + string[tup[i] + 1 - i::]
#
#     if not string:
#         return 'e'
#
#     return string
#
#
# def intersection(lst1, lst2):
#     """intersection of two lists"""
#     return list(set(lst1) & set(lst2))
#
#
# def replace(str1, str2):
#     """
#     replace 2 first elements of str1 by str2
#     Ex:
#     str1 = 'trung'
#     str2 = 'B'
#     replace(str1, str2) = 'Bung'
#     """
#     return str2 + str1[2:]

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
