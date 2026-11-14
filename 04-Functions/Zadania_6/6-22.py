def f(name):
    count = 0
    string = name[0]

    for x in name:
        if x == " ":
            string += name[count + 1]
        count += 1

    return string


if __name__ == "__main__":
    print(f("Internet of Things"))
    print(f("For Your Information"))
    print(f("Python"))