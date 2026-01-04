def f(product_code):
    result = 0
    suma = 0
    
    for x in product_code[0:3]:
        x = int(x)
        suma += x
    
    result = suma % 7
    
    if  result == int(product_code[3]):
        return True
    else:
        return False











if __name__ == "__main__":
    print(f("1082"))        # returns True
    print(f("2035"))        # returns True
    print(f("1114"))        # returns False
    print(f("7071"))        # returns False