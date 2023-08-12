inputArray = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
uniqueList = []
for i in inputArray:
    if i not in uniqueList:
        uniqueList.append(i)

uniqueList = sorted(uniqueList)
print(uniqueList[-1], uniqueList[-2])