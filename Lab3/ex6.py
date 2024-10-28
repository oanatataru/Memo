def count_unique_and_duplicates(lst):
    unique_elements = set(lst)
    total_unique = len(unique_elements)
    total_duplicates = len(lst) - total_unique

    return total_unique, total_duplicates


test_list = [1, 2, 3, 4, 4, 5, 6, 6, 7]
print(count_unique_and_duplicates(test_list))
