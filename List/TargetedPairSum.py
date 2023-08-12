numArr = [2,6,3,9,11]
target = 9
output = []

for i in range(0,len(numArr) - 1):
    pair = []
    for j in range(i+1, len(numArr) - 1):
        if numArr[i] + numArr[j] == target:
            pair.append(numArr[i])
            pair.append(numArr[j])
            output.append(pair)

print(output);