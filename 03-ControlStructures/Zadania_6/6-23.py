number = int(input("Enter number: "))
count = 1

for x in range(1,11):
    print(f"{number} x {count} = {number * count}")
    count += 1
print()



def f(liczba):
    numer = 1

    for y in range(1,11):
        print(f"{liczba} x {numer} = {liczba * numer}")
        numer += 1
    print()

if __name__ == "__main__":
    print(f(4))
    print(f(8))