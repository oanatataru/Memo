def count_vowels(str):
    vowels = "AEUIOaioue"
    count_vow = 0

    for char in str:
        if char in vowels:
            count_vow += 1

    return count_vow


user_string = input("Enter a string: ")
print(count_vowels(user_string))
