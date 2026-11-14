def f(binary_number):
    count = 0
    while count < len(binary_number):
        if int(binary_number[count]) == 0 or int(binary_number[count]) == 1:
            count += 1
            continue
        else:
            return False
    return True


if __name__ == "__main__":
    print(f("101101"))
    print(f("1311a10100"))

