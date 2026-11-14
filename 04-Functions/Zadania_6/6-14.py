def f(number1, number2, operator):
    output = 0
    if operator == '+':
        output = number1 + number2
    elif operator == "-":
        output = number1 - number2
    elif operator == "*":
        output = number1 * number2
    elif operator == "%":
        output = number1 % number2
    elif operator == "**":
        output = pow(number1, number2)

    return output


if __name__ == "__main__":
    print(f(2,3, "+"))
    print(f(2,3, "%"))
    print(f(2,3, "**"))
    print(f(2,3, "*"))
    print(f(2,3, "-")) 