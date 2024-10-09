def gcd(a, b):
    while b > 0:
        r = a % b
        a, b = b, r
    return a


def process(number_list):
    current_number = number_list[0]
    for number in number_list[1:]:
        current_number = gcd(current_number, number)
    return current_number


try:
    numbers = list(map(int, input("Enter some numbers: ").split()))
    print(f'The GCD of the given list is {process(numbers)}')
except ValueError:
    print("The list should contain only numbers!")

