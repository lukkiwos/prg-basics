array = [8, 2, 5, 1, 9]

array2 = []
index = 0

while index < len(array):
    x = array[index] * array[index]
    array2.append(x)
    index += 1

print(f"Array: {array}")
print()
print(f"2nd power: {array2}")