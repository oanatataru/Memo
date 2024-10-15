def combine_lists(*lists):
    max_len = max(len(current_list) for current_list in lists)

    result_list = []
    for i in range(max_len):
        tuple_item = tuple(current_list[i] if i < len(current_list) else None for current_list in lists)
        result_list.append(tuple_item)

    return result_list


list1 = [1, 2, 3]
list2 = [5, 6, 7]
list3 = ["a", "b", "c"]

result = combine_lists(list1, list2, list3)
print(result)
