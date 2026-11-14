def f(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1

    a = 0
    b = 1
    c = 0

    for x in range(2, n):
        c = b
        b = a + b
        a = c

    return b


if __name__ == "__main__":
    print(f(5))
    print(f(9))
    print(f(1))
    print(f(2))