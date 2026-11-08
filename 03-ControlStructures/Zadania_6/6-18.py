x = int(input("x = "))
y = int(input("y = "))

if x == 0 and y == 0:
    print(f"Point P({x},{y}) is in the CENTRE of the coordinate system")
elif x > 0 and y > 0:
    print(f"Point P({x},{y}) is in the FIRST quadrant of the coordinate system")
elif x < 0 and y > 0:
    print(f"Point P({x},{y}) is in the SECOND quadrant of the coordinate system")
elif x < 0 and y < 0:
    print(f"Point P({x},{y}) is in the THIRD quadrant of the coordinate system")
elif x > 0 and y < 0:
    print(f"Point P({x},{y}) is in the FOURTH quadrant of the coordinate system")

print()



def f(a,b):
    if a == 0 and b == 0:
        return 0
    elif a > 0 and b > 0:
        return 1
    elif a < 0 and b > 0:
        return 2
    elif a < 0 and b < 0:
        return 3
    elif a > 0 and b < 0:
        return 4


if __name__ == "__main__":
    print(f(0,0))
    print(f(3,3))
    print(f(-3,2))
    print(f(-3,-3))
    print(f(3,-3))