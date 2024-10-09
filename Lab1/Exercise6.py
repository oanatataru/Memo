def subtract_number(string):
    digits = "0123456789"
    number_found = 0
    ok = False

    for char in string:
        if char in digits:
            if ok == False:
                ok = True
            if (ok == True):
                number_found = number_found * 10 + int(char)
        elif ok == True:
            break
    return number_found


try:
    user_string = input("Enter a string in the console: ")
    print(subtract_number(user_string))
except ValueError:
    print("The number tou provided is not an int!")