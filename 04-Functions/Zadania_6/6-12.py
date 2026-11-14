def f(n):
    count = n - 1
    output = ""
    for x in range(n):
        if n == 1:
            output = "*"
        else:
            if x != count:
                output += "*"
                output += "/"
            else:
                output += "*"
    return output


def f1(a):
    output1 = ""
    for y in range(a):
        output1 += "*"
        if y != a - 1:
            output1 += "/"
    return output1



if __name__ == "__main__":
    print(f(4))
    print(f(1))
    print(f1(3))