###
# Checking whether the number
# entered from the keyboard is even or odd 
#
number = int(input('Enter number: '))

if number % 2 == 0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')




def f(liczba):
    if liczba % 2 == 0:
        return f"{liczba} jest parzysta"
    else:
        return f"{liczba} jest nieparzysta"


if __name__ == "__main__":
    print(f(4))
    print(f(5))
    