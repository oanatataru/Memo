def third_char_key(tuple_el):
    return tuple_el[1][2] if len(tuple_el[1]) > 2 else ""


def order_tuples(tuples):
    sorted_list = sorted(tuples, key=third_char_key)
    return sorted_list


tuples_list = [('abc', 'bcd'), ('abc', 'zza')]
print(order_tuples(tuples_list))


