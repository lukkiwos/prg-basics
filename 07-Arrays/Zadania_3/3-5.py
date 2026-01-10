array = [15, 8, 31, 47, 2, 19]

suma = 0

for x in array:
    suma += x

arithmetic_mean = suma / len(array)

print(f"Array: {array}")
print(f"Arithmetic mean: {arithmetic_mean:.2f}")