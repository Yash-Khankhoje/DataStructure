dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

for key, value in dict2.items():
    if key not in dict1:
        dict1[key]= value
    else:
        dict1[key] = dict1[key] + value

print(dict1)