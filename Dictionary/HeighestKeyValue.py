my_dict = {'a': 5, 'b': 9, 'c': 2}
maxKey = 'a'
maxVal = my_dict['a']
for key,value in my_dict.items():
    if value > maxVal:
        maxKey = key
        maxVal = value

print(maxKey)