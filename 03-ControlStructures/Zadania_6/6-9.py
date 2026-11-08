name = input("Enter name: ")

if name[-1] == "a":
    print(name)
print()



def f(name1):
    if name1[-1] == "a":
        return name1


if __name__ == "__main__":
    print(f("Anna"))
    print(f("Bartek"))