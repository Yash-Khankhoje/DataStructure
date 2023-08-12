binaryList = [1,0,0,1,0,1,1,0,1,0,0,1,1,1,0,0,1,1,1]
chances = int(input("Please enter the number of chances: "))
maxLength = 0

for i in range(0, len(binaryList)):
    count = 0
    chanceCount = 0
    for j in range(i, len(binaryList)):
        if binaryList[j] == 1:
            print(binaryList[j])
            count += 1
        else:
            print("no")
            chanceCount += 1
            if chanceCount > chances:
                chanceCount = 0
                if maxLength <= count:
                    maxLength = count
                count = 0
            else: 
                count += 1
    print()

print(maxLength)
print(len(binaryList))