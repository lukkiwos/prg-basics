array = [15, 8, 31, 47, 2, 19]

index = 0
suma = 0

while index < len(array):
    suma += array[index]
    index += 1

arithmetic_mean = suma / len(array)

print(f"Array: {array}")
print(f"Arithmetic mean: {arithmetic_mean:.2f}")