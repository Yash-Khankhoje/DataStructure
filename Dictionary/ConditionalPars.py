my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

for key, value in my_dict.items():
    if value % 2 == 0:
        print(key, ":", value)