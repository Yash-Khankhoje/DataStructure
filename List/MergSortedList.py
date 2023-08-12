lst = [4,6,8,9,10,12]
lst2 = [1,3,7,11,12]
output = []

i = 0
j = 0
while i < len(lst) and j < len(lst2):
    if lst[i] > lst2[j]:
        output.append(lst2[j])
        j += 1
    else:
        output.append(lst[i])
        i += 1

if j < len(lst2):
    output.extend(lst2[j:])
elif i < len(lst):
    output.extend(lst[i:])
print(output)
