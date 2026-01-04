def f(x, y):

    suma = 0

    for i in range(x, y + 1):
        if i % 2 == 0 and i % 3 == 0 and i % 4 != 0:
            suma += i

    return suma



if __name__ == "__main__":
    print(f(1,20))      # returns 24
    print(f(10,30))     # return 48