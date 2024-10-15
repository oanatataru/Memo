from math import sqrt


def check_prime(number):
    prime_flag = 0
    if number <= 1:
        return 0
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            prime_flag = 1
            break
    # the number is not prime
    if prime_flag == 1:
        return 0
    # the number is prime
    else:
        return 1


def check_list(numbers_list):
    prime_numbers = []
    for i, number in enumerate(numbers_list):
        if check_prime(number):
            prime_numbers.append(number)
    return prime_numbers


user_numbers = input("Write a list of numbers: ")
try:
    user_numbers = list(map(int, user_numbers.split()))
    print(check_list(user_numbers))
except ValueError:
    print("The list should only be int numbers separated by a space!")



