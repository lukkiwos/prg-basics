number = int(input("Enter number: "))

if number > 0:
    print(f"Number {number} is positive")
elif number < 0:
    print(f"Number {number} is negative")
elif number == 0:
    print(f"Number is 0")
else:
    print("Error")
print()


def f(liczba):
    if liczba > 0:
        return f"Liczba {liczba} jest dodatnia"
    elif liczba < 0:
        return f"Liczba {liczba} jest negatywna"
    elif liczba == 0:
        return f"Liczba jest zerem"
    

if __name__ == "__main__":
    print("Sprawdzanie funkcji: ")
    print(f(1))
    print(f(-1))
    print(f(0))