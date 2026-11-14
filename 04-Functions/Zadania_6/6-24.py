def f(expression):
    suma = int(expression[0])

    for x in range(1, len(expression), 2):
        if expression[x] == "+":
            suma += int(expression[x+1])
        elif expression[x] == "-":
            suma -= int(expression[x+1])

    return suma


if __name__ == "__main__":
    print(f("2+3"))
    print(f("3+8+1"))
    print(f("2+3-4+5-0"))