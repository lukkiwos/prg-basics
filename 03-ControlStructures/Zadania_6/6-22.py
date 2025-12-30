for i in range(1,31):

    if i % 3 == 0 and i % 5 == 0:
        print("BINGO")
    elif i % 3 == 0:
        print("THREE")
    elif i % 5 == 0:
        print("FIVE")
    else:
        print(i)
print()
print()
print()
print()
print()





def f():
    for i in range(1,31):
        if i % 3 == 0 and i % 5 == 0:
            print("BINGO")
        elif i % 3 == 0:
            print("THREE")
        elif i % 5 == 0:
            print("FIVE")
        else:
            print(i)
        


if __name__ == "__main__":
    print(f())
    print()
    print()
    print()
    print()





def f1():
    result = []
    for i in range(1,31):
        if i % 3 == 0 and i % 5 == 0:
            result.append("BINGO")
        elif i % 3 == 0:
            result.append("TRZY")
        elif i % 5 == 0:
            result.append("PIĘĆ")
        else:
            result.append(str(i))
    return result


if __name__ == "__main__":
    for line in f1():
        print(line)