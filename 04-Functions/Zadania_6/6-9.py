def f(number, even):
    suma = 0

    for x in str(number):
        x = int(x)
        if even:
            if x % 2 == 0:
                suma += x
        else:
            if x % 2 != 0:
                suma += x
    return suma


if __name__ == "__main__":
    print(f(3124,True))
    print(f(3124,False))
    print(f(20576,False))
    print(f(20576,True))
    print(f(13115,True))