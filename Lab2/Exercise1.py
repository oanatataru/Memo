def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num-2)


try:
    number = int(input("Enter a number: "))
    print(f'These are the first {number} Fibonacci numbers:')
    for i in range(0, number):
        print(fibonacci(i), end=" ")
except ValueError:
    print("This is not a valid number!")
