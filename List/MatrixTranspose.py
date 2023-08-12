matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

rows = 0
columns = 0
tempArray = []
transposedMatrix = []

for i in matrix:
    rows += 1
    for j in i:
        tempArray.append(j)

tempArray.reverse()
columns = len(tempArray) / rows
rowCount = 0
num = 1
tempArrTwo = []
while rowCount != rows:
    rowCount += 1
    tempArrTwo.extend(tempArray[int(columns)-num::int(columns)])
    transposedMatrix.append(tempArrTwo)
    tempArrTwo = []
    num += 1

print(transposedMatrix)
    
