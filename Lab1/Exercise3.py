def count(main_string, substring):
    return main_string.count(substring)


first_string = input("Enter the first string: ")
second_string = input("Enter the second string: ")

occurrences = count(second_string, first_string)
print(f"The number of occurrences of '{first_string}' in the second string is: {occurrences}")
