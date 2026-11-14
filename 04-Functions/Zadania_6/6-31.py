def f(x, n):
    if n == 0:
        return 1

    if n > 1:
        return x * f(x, n - 1)



if __name__ == "__main__":
    print(f(5, 3))