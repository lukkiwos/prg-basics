def f(product_code):
    suma = 0
    count = 0

    while count < len(product_code) - 1:
        x = product_code[count]
        suma += int(x)
        count += 1
    
    liczba = int(product_code[-1])

    if suma % 7 == liczba:
        return True
    else:
        return False


if __name__ == "__main__":
    print(f("1082"))
    print(f("2035"))
    print(f("1114"))
    print(f("7071"))
    