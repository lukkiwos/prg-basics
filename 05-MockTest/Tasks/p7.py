def f(n):
    a = 0
    b = 1

    if n == 1:
        return 0
    elif n == 2:
        return 1

    for x in range(3, n + 1):
        c = a + b
        a = b
        b = c

    return b




if __name__ == "__main__":
    print(f(5))
    print(f(9))



# UDAŁO mi się zrobić samemu