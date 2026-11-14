def f(x,y):
    count = 0
    for char in range(x, y + 1):
        if char < 0:
            char = abs(char)
            if char % 2 == 0:
                count += 1

    return count


if __name__ =="__main__":
    print(f(-7,8))
    print(f(-1,11))