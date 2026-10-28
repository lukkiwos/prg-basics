###
# Program for testing built-in functions
#
max_number = max(7,5,6,3,8,2)
print(f"Max number of 7,5,6,3,8,2 is: {max_number}")

min_number = min(4,7,2,3,9,8)
print(f"Min number of 4,7,2,3,9,8 is: {min_number}")

str_length = len("computer science")
print(f"The number of characters in 'computer science' is: {str_length}")

letter = input("Enter letter from the keyboard: ")
print(f"Letter read from the keyboard is: {letter}")

number = int("20303")
print(f"Number representing the string '20303': {number}")

binary = bin(304)
print(f"Binary string representing decimal number '304': {binary}")

hexadecimal = hex(304)
print(f"Hexadecimal string representing decimal number '304': {hexadecimal}")

integer = ord("€")
print(f"Integer representing the Unicode code of the € sign: {integer}")

value = abs(-17)
print(f"Absolute value of '-17': {value}")
