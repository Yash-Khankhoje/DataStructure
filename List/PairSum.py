mainList = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
target = 7
outputList = []

for i in range(0, len(mainList)):
    temp = []
    for j in range(i, len(mainList)):
        if mainList[i] + mainList[j] == target :
            temp.append(mainList[i])
            temp.append(mainList[j])
            outputList.append(temp)
            break

print(outputList)

