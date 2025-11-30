###
# Program for testing built-in functions
#
max_number = max(7,5,6,3,8,2)
print(f'Max number of 7,5,6,3,8,2 is: {max_number}')

min_number = min(4,7,2,3,9,8)
print(f'Min number of 4,7,2,3,9,8 is: {min_number}')

str_length = len("computer science")
print(f'The number of characters in "computer science" is: {str_length}')


letter_read = input('Enter "letter": ')
print(f'Letter read from the keyboard is: {letter_read}')

number_representing = int('20303')
print(f'The number which represents decimal number is: {number_representing}')

binary_string = bin(304)
print(f'Binary string representing decimal number is: {binary_string}')

hexadecimal_string = hex(304)
print(f'Hexadecimal string representing decimal number is: {hexadecimal_string}')

integer_unicode = ord('€')
print(f'Integer representing the Unicode code is: {integer_unicode}')

absolute_value = abs(-17)
print(f'Absolute value is: {absolute_value}')