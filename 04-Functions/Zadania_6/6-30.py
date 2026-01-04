def sum_natural(n):

    if n == 1:
        suma = 1

    elif n > 1:
        suma = n + sum_natural(n - 1)

    return suma


if __name__ == "__main__":
    print(sum_natural(10))