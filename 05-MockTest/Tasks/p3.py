def f(name):

    name = name.split()
    result = ""

    for x in name:
        result += x[0]

    return result


if __name__ == "__main__":
    print(f("Internet of Things"))
    print(f("For Your Information"))
    print(f("Python"))



# NIE udało mi się zrobić samemu