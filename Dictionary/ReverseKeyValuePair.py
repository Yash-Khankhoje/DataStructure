my_dict = {'a': 1, 'b': 2, 'c': 3}
outputDict = {}

for key, value in my_dict.items():
    outputDict[value] = key

print(outputDict)