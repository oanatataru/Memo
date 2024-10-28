from itertools import combinations

def set_operations(*sets):
    result = {}
    for set_a, set_b in combinations(sets, 2):
        result[f"{set_a} | {set_b}"] = set_a | set_b
        result[f"{set_a} & {set_b}"] = set_a & set_b
        result[f"{set_a} - {set_b}"] = set_a - set_b
        result[f"{set_b} - {set_a}"] = set_b - set_a

    return result


sets = ({1, 2}, {2, 3})
print(set_operations(*sets))
