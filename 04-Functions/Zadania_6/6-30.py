def f(n):
    if n == 1:
        return 1

    if n > 1:
        return n + f(n - 1)

if __name__ == "__main__":
    print(f(10))