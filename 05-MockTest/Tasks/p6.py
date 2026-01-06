def f(number, even):

    result = 0

    if even:
        for x in str(number):
            x = int(x)
            if x % 2 == 0:
                result += x
    else:
        for x in str(number):
            x = int(x)
            if x % 2 != 0:
                result += x

    return result




if __name__ == "__main__":
    print(f(3124, True))
    print(f(3124, False))
    print(f(20576, False))
    print(f(20576, True))
    print(f(13115, True))




# UDAŁO mi się zrobić samemu