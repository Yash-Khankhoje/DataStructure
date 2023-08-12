A = [[2,4],[3,4]]

my_D = {}
temp = []
for i in A:
    for j in range(i[0],i[1]+1):
        temp.append(j)

for i in temp:
    my_D[i] = temp.count(i)


output = []

for i in range(0, len(A) - 1):
    output.append(0)

match = 0
notMatch = 0
for key in my_D:
    if my_D[key] != len(A):
        notMatch += 1
    else:
        match += 1

output.append(notMatch)
output.append(match)
print(output)