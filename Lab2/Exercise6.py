def process(x, *lists):
    unique_items = []
    counts = []

    for list in lists:
        for item in list:
            if item not in unique_items:
                unique_items.append(item)
                counts.append(1)
            else:
                index = unique_items.index(item)
                counts[index] += 1

    result = []
    for i in range(len(unique_items)):
        if counts[i] == x:
            result.append(unique_items[i])

    return result


list1 = [1, 2, 3]
list2 = [2, 3, 4]
list3 = [4, 5, 6]
list4 = [4, 1, "test"]
x = 2

result = process(x, list1, list2, list3, list4)
print(result)
