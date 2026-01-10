array = [2, 6, 4, 9, 7]


def star(n):
    x = "*" * n

    return x


for x in array:
    print(f"{x}: {star(x)}")

