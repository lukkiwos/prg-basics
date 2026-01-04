def f(number):
    suma = 0

    for x in str(number):
        if str(number).count(x) > 1:
            suma += int(x)

    return suma


if __name__ == "__main__":
    print(f(1027))          # returns 0
    print(f(230335))        # returns 9
    print(f(513553007))     # returns 21