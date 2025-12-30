###
# Checking whether the number
# entered from the keyboard is even or odd 
#
number = int(input('Enter number: '))

if number % 2 == 0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')
print()


def f(number):
    if number % 2 == 0:
        return "Number is even"
    else:
        return "Number is odd"


if __name__ == "__main__":
    print(f(5))