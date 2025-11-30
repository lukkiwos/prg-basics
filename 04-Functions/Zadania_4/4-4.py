###
# Calculates the sum of the digits in a number
#

def sum_digits(number):
    absolute_number = abs(number)                        # 2)
    string_number = str(absolute_number)                # 3)
    total_sum = 0
    
    for digit_char in string_number:
        digit_value = int(digit_char)
        total_sum += digit_value
    return total_sum


any_number = int(input('Enter integer number: '))       # 1)

result = sum_digits(any_number)

print(f'The sum of the digits in the number {any_number} is {result}')