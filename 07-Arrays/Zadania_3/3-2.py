array = [15, 8, 31, 47, 2, 19]

array2 = []
index = len(array) - 1

while index >= 0:
    array2.append(array[index])
    index -= 1

print(f"Existed array: {array}")
print()
print(f"Reverse array: {array2}")