def find_loop(mapping):
    visited = set()
    result = []
    current_key = "start"

    while current_key not in visited:
        visited.add(current_key)
        current_value = mapping[current_key]
        if current_value not in visited:
            result.append(current_value)
        current_key = current_value

    return result


# Test
mapping = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
print(find_loop(mapping))
