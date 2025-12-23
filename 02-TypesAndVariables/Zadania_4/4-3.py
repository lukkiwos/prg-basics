a = 3
b = 5

print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')
print()


def f(x, y, symbol):
    wynik = 0
    if symbol == "+":
        wynik = x + y
    elif symbol == "-":
        wynik = x - y
    elif symbol == "*":
        wynik = x * y
    elif symbol == "/":
        wynik = x / y
    return wynik

if __name__ == "__main__":
    print(f(14, 19, "+"))