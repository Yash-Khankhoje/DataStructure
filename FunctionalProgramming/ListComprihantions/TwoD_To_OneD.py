lst = [[1,2,3],[4,5,6],[7,8,9]]
lst2 = [item for subLst in lst for item in subLst]
print(lst2)