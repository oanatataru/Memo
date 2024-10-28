def validate_dict(rules, dictionary):
    for key, prefix, middle, suffix in rules:
        if key not in dictionary:
            return False
        value = dictionary[key]

        if not value.startswith(prefix) or middle not in value or not value.endswith(suffix):
            return False

        if value.startswith(middle) or value.endswith(middle):
            return False

    return True


rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
dictionary = {"key1": "come inside, it's too cold out", "key3": "start with some middle part and ends in winter"}

print(validate_dict(rules, dictionary))
