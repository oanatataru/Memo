def my_function(*args, **kwargs):
    kw_values = set(kwargs.values())

    count = sum(1 for arg in args if arg in kw_values)

    return count


result = my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5)
print(result)
