###
# A program for checking clothing sizes
# S: Small size, M: Medium size, L: Large size
# XL: Extra large size or Incorrect symbol (if entered symbol
# dirrerent than S, M, L, XL)
#
size = input('Enter size symbol (S/M/L/XL): ')

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


def f(size):
    if size == "S":
        return "S: Small size"
    elif size == "M":
        return "M: Medium size"
    elif size == "L":
        return "L: Large size"
    elif size == "Xl":
        return "XL: Extra large size"
    return size


if __name__ == "__main__":
    print(f("M"))