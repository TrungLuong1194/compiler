def is_child_list(a, b):
    """
    Checking elements of list a on list b
    eg: [x, y] on [x, y, z]
    """
    count = 0
    for i in range(len(a)):
        if a[i] in b:
            count += 1

    if count == len(a):
        return True

    return False


def remove_string_by_index(string, tup):
    """Remove multiple characters of string by index. Indexes are determined in tuple"""
    for i in range(len(tup)):
        string = string[0:tup[i] - i:] + string[tup[i] + 1 - i::]

    return string


def intersection(lst1, lst2):
    """intersection of two lists"""
    return list(set(lst1) & set(lst2))


def replace(str1, str2):
    """
    replace 2 first elements of str1 by str2
    Ex:
    str1 = 'trung'
    str2 = 'B'
    replace(str1, str2) = 'Bung'
    """
    return str2 + str1[2:]
