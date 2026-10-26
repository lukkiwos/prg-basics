###
# A program for checking clothing sizes
# S: Small size, M: Medium size, L: Large size
# XL: Extra large size or Incorrect symbol (if entered symbol
# dirrerent than S, M, L, XL)
#
size = input('Enter size symbol: ')

if size == 'S':
    print('S: Small size')
elif size == 'M':
    print("M: Medium size")
elif size == "L":
    print("L: Large size")
elif size == "XL":
    print("XL: Extra large size")
else:
    print("Incorrect symbol")
print()


def f(rozmiar):
    if rozmiar == "S":
        return "S: Small size"
    elif rozmiar == "M":
        return "M: Medium size"
    elif rozmiar == "L":
        return "L: Large size"
    elif rozmiar == "XL":
        return "XL: Extra large size"
    else:
        return "Incorrect symbol"


if __name__ == "__main__":
    print(f("S"))
    print(f("M"))
    print(f("L"))
    print(f("XL"))
    print(f("T"))