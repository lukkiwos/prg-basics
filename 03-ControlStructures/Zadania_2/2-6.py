number = int(input("Enter number: "))

if number > 0:
    print(f"Number {number} is positive")
elif number < 0:
    print(f"Number {number} is negative")
else:
    print(f"Number is 0")
print()



def f(liczba):
    if liczba > 0:
        return f"Liczba {liczba} jest pozytywna"
    elif liczba < 0:
        return f"Liczba {liczba} jest negatywna"
    else:
        return "Liczba jest 0"


if __name__ == "__main__":
    print(f(7))
    print(f(1))
    print(f(0))
    print(f(-1))
    print(f(-4))