name = input("Enter name: ")

if name.endswith('a'):
    print(f"{name} -- Polish female name")

print()






def f(name):
    if name.endswith("a"):
        return f"{name} --------- Polish female name"
    


if __name__ == "__main__":
    print(f("Anna"))