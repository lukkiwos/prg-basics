decimal_number = int(input("Enter decimal number: "))

number = decimal_number

remainders = []

while decimal_number > 0:
    remainder = decimal_number % 2
    remainders.append(remainder)
    decimal_number = decimal_number // 2

binary = ''
for i in reversed(remainders):
    binary += str(i)


print(f"{number}(10) = {binary}(2)")
print()






def f(number):
    x = bin(number)
    return f"{number}(10) = {x}(2)"


if __name__ == "__main__":
    print(f(15))
    print()





def f1(number):
    remainders = []
    
    number1 = number
    while number > 0:
        remainder = number % 2
        remainders.append(remainder)
        number = number // 2

    binary = ""
    for i in reversed(remainders):
        binary += str(i)

    return f"{number1}(10) = {binary}(2)"


if __name__ == "__main__":
    print(f1(15))
