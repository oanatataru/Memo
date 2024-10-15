def difference(first_list, second_list):
    difference_list = []
    for element in first_list:
        if element not in second_list:
            difference_list.append(element)
    return difference_list


def list_operations(a, b):
    intersection = [element for element in a if element in b]

    # not a reference, but a copy!
    union = a.copy()
    for element in b:
        if element not in union:
            union.append(element)
    union.sort()

    print(f'Intersection of A and B: {intersection}')
    print(f'Union of A and B: {union}')
    print(f'Difference A - B: {difference(a, b)}')
    print(f'Difference B - A: {difference(b, a)}')


list_a = [1, 2, 3, 4, 5]
list_b = [1, 2, 6, 8, 9]
list_operations(list_a, list_b)

