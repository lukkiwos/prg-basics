def f(n):
    output = ""
    for x in range(1, n + 1):
        output += str(x)

    return output


if __name__ == "__main__":
    print(f(11))
    print(f(4))