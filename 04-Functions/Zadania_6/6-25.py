def f(x,y):
    suma = 0

    for a in range(x,y + 1):
        if a % 2 == 0 and a % 3 == 0 and a % 4 != 0:
            suma += a
        
    return suma


if __name__ == "__main__":
    print(f(1,20))
    print(f(10,30))