myTwoD_List = [[1,2,3],[4,5,6],[7,8,9]]
sum = 0

for i in range(0, len(myTwoD_List)):
    for j in range(i, len(myTwoD_List[i])):
        sum += myTwoD_List[i][j]
        break

print(sum)