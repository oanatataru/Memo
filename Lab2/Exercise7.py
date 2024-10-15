def check_palindrome(number):
    reverse = 0
    c = number
    while c != 0:
        reverse = reverse * 10 + c % 10
        c = c // 10

    return reverse == number


def check_list(number_list):
    palindrome_list = []
    greatest_palindrome = -1
    for number in number_list:
        if check_palindrome(number):
            palindrome_list.append(number)
            if number > greatest_palindrome:
                greatest_palindrome = number

    return palindrome_list, greatest_palindrome


print(check_list([1, 2, 101, 10001]))

