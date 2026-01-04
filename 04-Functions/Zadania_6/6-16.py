def f(n):
    
    if n == 1:
        return 0
    elif n == 2:
        return 1

    a = 0
    b = 1

    for x in range(3, n + 1):
        c = a + b
        a = b
        b = c
    
    return b




if __name__ == "__main__":
    print(f(5))     # returns 3
    print(f(9))     # returns 21