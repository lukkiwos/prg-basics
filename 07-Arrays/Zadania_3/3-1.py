# An array contains integer numbers: 34,7,19,4,21,8. 
# Create a program that calculates 
# and prints the number of even values in the array. 
# Use the ‘while’ loop statement.


array = [34, 7, 19, 4, 21, 8]

count = 0
even = 0

while count < len(array):
    if array[count] % 2 == 0:
        even += 1
    count += 1


print(f"Number of even values in array is: {even}")