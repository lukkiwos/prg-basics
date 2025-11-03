###
# Checking whether the number
# entered from the keyboard is even or odd 
#
while True:
    number = int(input('Enter number: '))

    if number % 2 == 0:
        print(f'{number} is even')
    else:
        print(f'{number} is odd')