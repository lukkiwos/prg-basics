###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    number = abs(any_number)
    number = str(number)
    sum = 0
    
    for x in number:
        y = int(x)
        sum += y

    return sum



any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is: {result}')
print()
print()





def f(number):
    number = abs(number)
    number = str(number)
    sum = 0
    
    for x in number:
        y = int(x)
        sum += y

    return f"Suma podanych liczb to: {sum}"



if __name__ == "__main__":
    print(f(54321))