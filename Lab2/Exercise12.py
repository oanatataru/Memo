def rhyme_generator(words_list):
    rhyme_dict = {}

    for word in words_list:
        rhyme_key = word[-2:] if len(word) >= 2 else word

        if rhyme_key in rhyme_dict:
            rhyme_dict[rhyme_key].append(word)
        else:
            rhyme_dict[rhyme_key] = [word]

    return list(rhyme_dict.values())


print(rhyme_generator(['ana', 'banana', 'carte', 'arme', 'parte']))

