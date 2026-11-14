def f(n):
    # 0! = 1, 1! = 1
    if n == 0 or n == 1:
        return 1

    # n! = n * (n-1)!
    if n > 1:
        return n * f(n - 1)


if __name__ == "__main__":
    print(f(5))