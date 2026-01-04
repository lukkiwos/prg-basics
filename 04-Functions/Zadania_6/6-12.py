def f(number):
    lista = number * ["*"]
    result = "/".join(lista)
    
    return result

if __name__ == "__main__":
    print(f(4))
    print(f(1))