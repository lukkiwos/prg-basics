for x in range(1,31):
    if x % 3 == 0 and x % 5 == 0:
        print("BINGO")
    elif x % 3 == 0:
        print("THREE")
    elif x % 5 == 0:
        print("FIVE")
    else:
        print(x)
print()


def f(x,y):
    for char in range(x, y + 1):
        if char % 3 == 0 and char % 5 == 0:
            print("BINGO")
        elif char % 3 == 0:
            print("THREE")
        elif char % 5 == 0:
            print("FIVE")
        else:
            print(char)


if __name__ == "__main__":
    print(f(1,15))