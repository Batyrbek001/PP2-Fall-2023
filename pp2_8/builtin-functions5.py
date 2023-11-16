def true(tup):
    return all(tup)

str = input()
str_list = str.split()
tuple = tuple(map(lambda x: x.lower() == 'true', str_list))
result = true(tuple)
print(result)