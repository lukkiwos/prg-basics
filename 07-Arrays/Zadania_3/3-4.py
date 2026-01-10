array = [-15, 8, -31, 47, -2, 19]

max_number = array[0]
min_number = array[0]
index = 0

while index < len(array):
    if array[index] > max_number:
        max_number = array[index]
    if array[index] < min_number:
        min_number = array[index]

    index += 1

print(f"Maximum number is: {max_number}")
print(f"Minimum number: {min_number}")