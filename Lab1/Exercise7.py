def count_bits(number):
    count = 0
    while number > 0:
        if number % 2 == 1:
            count += 1
        number = number // 2
    return count


number = int(input("Enter a number: "))
one_bits_count = count_bits(number)
print(f"The number {number} has {one_bits_count} bits with value '1'.")
