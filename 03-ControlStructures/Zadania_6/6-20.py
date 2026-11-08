decimal = int(input("Enter decimal number: "))
decimal1 = decimal
binary = ""

while decimal > 0:
    remainder = decimal % 2
    decimal = decimal // 2
    binary = str(remainder) + binary
    
print(f"{decimal1}(10) = {binary}(2)")
print()



def f(number):
    bin = ""

    while number > 0:
        reszta = number % 2
        number = number // 2
        bin = str(reszta) + bin

    return bin


if __name__ == "__main__":
    print(f(12))
    print(f(60))