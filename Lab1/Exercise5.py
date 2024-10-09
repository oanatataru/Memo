def check_palindrome(number):
    reverse = 0
    c = number
    while c != 0:
        reverse = reverse * 10 + c % 10
        c = c // 10

    return reverse == number


print(check_palindrome(1001))