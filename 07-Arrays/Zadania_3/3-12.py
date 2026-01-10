array = [2, 3, 2, 5, 8, 1, 9, 8]

unique = []

for x in array:
    if array.count(x) == 1:
        unique.append(x)

print(f"Array: {", ".join(map(str, array))}")
print(f"Unique elements: {", ".join(map(str, unique))}")