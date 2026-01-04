###
# Program for testing built-in functions
#
max_number = max(7,5,6,3,8,2)
print(f'1 - Max number of 7,5,6,3,8,2 is: {max_number}')
print()

min_number = min(4,7,2,3,9,8)
print(f'2 - Min number of 4,7,2,3,9,8 is: {min_number}')
print()

str_length = len("computer science")
print(f'3 - The number of characters in "computer science" is: {str_length}')
print()

letter = input("4 - Enter letter: ")
print(f"Letter read from the keyboard is: {letter}")
print()

string = int("20303")
print(f"5 - Number representing the string is: {string}")
print()

binary = bin(304)
print(f"6 - Binary string representing decimal number 304 is: {binary}")
print()

hexadecimal = hex(304)
print(f"7 - Hexadecimal string representing decimal number 304 is: {hexadecimal}")
print()

unicode = ord("€")
print(f"8 - Integer representing the Unicode code of the € sign is: {unicode}")
print()

absolute = abs(-17)
print(f"9 - Absolute value of -17 is: {absolute}")
print()
