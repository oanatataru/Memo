def convert_to_snake_case(string):
    result = ""

    for char in string:
        if char.isupper():
            if result:
                result += "_"
            result += char.lower()
        else:
            result += char

    return result


user_string = input("Enter a string in UpperCaseCamel: ")
print(convert_to_snake_case(user_string))

