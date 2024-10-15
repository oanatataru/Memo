def process(flag=True, strings=None, x=1):
    if strings is None:
        strings = []
    result = []

    if flag:
        for string in strings:
            characters = [char for char in string if not ord(char) % x]
            result.append(characters)
    else:
        for string in strings:
            characters = [char for char in string if ord(char) % x]
            result.append(characters)

    return result


print(process(flag=False, strings=["test", "hello", "lab002"], x=2))

