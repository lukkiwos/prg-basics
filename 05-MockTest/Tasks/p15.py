def f(a,b):

    suma = 0

    for x in range(a, b + 1):
        if x % 3 == 0:
            suma += x

    return suma




if __name__ == "__main__":
    print(f(1,6))
    print(f(2,10))



# UDAŁO mi się zrobić