array1 = [2, 4]
array2 = [1, 2, 3, 4, 5]


is_subset = True

for x in array1:
    if x not in array2:
        is_subset = False
        break

print(is_subset)
    