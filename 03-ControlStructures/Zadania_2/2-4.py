###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
operator = input("Enter mathematical operator (+,-,*,/): ")

if operator == "+":
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
elif operator == "*":
    result = number1 * number2
elif operator == "/":
    result = number1 / number2
else:
    print("Incorrect operator")

# print result
print(f'{number1} {operator} {number2} = {result}')
print()


def f(liczba1, znak, liczba2):

    if znak == "+":
        wynik = liczba1 + liczba2
    elif znak == "-":
        wynik = liczba1 - liczba2
    elif znak == "*":
        wynik = liczba1 * liczba2
    elif znak == "/":
        wynik = liczba1 / liczba2

    return f"{liczba1} {znak} {liczba2} = {wynik}"


if __name__ == "__main__":
    print(f(2, "+" ,3))
    print(f(2, "*" ,4))
    print(f(3, "-" ,5))
    print(f(5, "*" ,6))