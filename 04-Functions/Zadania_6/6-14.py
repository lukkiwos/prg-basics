def f(number1, number2, operator):
    result = 0

    if operator == "+":
        result = number1 + number2
    elif operator == "-":
        result = number1 - number2
    elif operator == "*":
        result = number1 * number2
    elif operator == "%":
        result = number1 % number2
    elif operator == "**":
        result = number1 ** number2
    
    return result





if __name__ == "__main__":
    print(f(2,3, "+"))      # returns 5
    print(f(2,3, "%"))      # returns 2
    print(f(2,3, "**"))     # returns 8
    print(f(2,3, "*"))      # returns 6
    print(f(2,3, "-"))      # returns -1