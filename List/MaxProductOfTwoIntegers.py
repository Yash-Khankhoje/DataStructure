arr = [1,7,3,4,5,9]
arrTwo = []
for i in arr:
    if i not in arrTwo:
        arrTwo.append(i)

arrTwo = sorted(arrTwo)
print(arrTwo[-1] * arrTwo[-2])