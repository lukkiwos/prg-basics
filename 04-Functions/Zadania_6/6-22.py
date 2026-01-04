def f(name):
    word = name.split()

    akronim = ""

    for x in word:
        akronim += x[0]

    return akronim




if __name__ == "__main__":
    print(f("Internet of Things"))          # returns "IoT"
    print(f("For Your Information"))        # returns "FYI"
    print(f("Python"))                      # returns "P"