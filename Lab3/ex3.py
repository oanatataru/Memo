def compare_dicts(dict1, dict2):
    if len(dict1) != len(dict2):
        return False

    for key in dict1:
        if key not in dict2:
            return False

        value1 = dict1[key]
        value2 = dict2[key]

        if isinstance(value1, dict) and isinstance(value2, dict):
            if not compare_dicts(value1, value2):
                return False
        elif isinstance(value1, list) and isinstance(value2, list):
            if len(value1) != len(value2) or any(
                    not compare_dicts(v1, v2) if isinstance(v1, dict) and isinstance(v2, dict) else v1 != v2 for v1, v2
                    in zip(value1, value2)):
                return False
        elif isinstance(value1, set) and isinstance(value2, set):
            if value1 != value2:
                return False
        else:
            if value1 != value2:
                return False

    return True


# Test the function
dict_a = {'a': 1, 'b': {'c': 2, 'd': [1, 2]}, 'e': {1, 2, 3}}
dict_b = {'a': 1, 'b': {'c': 2, 'd': [1, 2]}, 'e': {1, 2, 3}}
print(compare_dicts(dict_a, dict_b))
