def power(x, n):

    if x == 0:
        return 0
    elif n == 0:
        return 1
    elif n > 0:
        return x * power(x, n - 1)
    


if __name__ == "__main__":
    print(power(5,3))