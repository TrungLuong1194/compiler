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
