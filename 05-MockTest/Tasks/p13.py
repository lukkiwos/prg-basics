def f(product_code):

    suma = int(product_code[0]) + int(product_code[1]) + int(product_code[2])

    x = suma % 7 

    if int(product_code[3]) == x:
        return True
    return False


if __name__ == "__main__":
    print(f("1082"))
    print(f("2035"))




# UDAŁO mi się zrobić