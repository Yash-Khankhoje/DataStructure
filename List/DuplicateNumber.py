userInput = [1, 1, 2, 2, 3, 4, 5]
outputList = []
for i in userInput:
    if i not in outputList:
        outputList.append(i)

print(outputList)