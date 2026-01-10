array = [7,9,2,4,5,6]

array1 = []
for x in array:
    if x % 2 == 0:
        array1.append(x)

for x in array:
    if x % 2 != 0:
        array1.append(x)

print(array)
print()
print(array1)