def char_count(input_string):
    char_dict = {}
    for char in input_string:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

test_string = "Ana has apples."
print(char_count(test_string))
