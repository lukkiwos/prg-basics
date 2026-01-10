###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4]

print(f"The array: {arr}")
print(f'Number of elements: {len(arr)}')
print(f'First value {arr[0]}')
print(f'Second value {arr[1]}')
print(f"Last value: {arr[-1]}")
print(f"Last but one value: {arr[3]}")
print(f"Sum of the first and last value: {arr[0] + arr[-1]}")
print(f"Middle value: {arr[len(arr) // 2]}")

array = ""
for x in arr:
    x = str(x)
    array += x
    array += " "

print(f"All array values separated by a single space: {array}")