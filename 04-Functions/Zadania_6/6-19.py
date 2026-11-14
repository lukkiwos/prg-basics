def f(number):
    repeated = 0
    sum_repeated = 0

    number = str(number)
    for x in number:
        repeated = number.count(x)

        x = int(x)
        if repeated > 1:
            sum_repeated += x

    return sum_repeated



if __name__ == "__main__":
    print(f(1027))
    print(f(230335))
    print(f(513553007))