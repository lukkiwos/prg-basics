x = int(input("Enter x: "))
y = int(input("Enter y: "))

if x == 0 and y == 0:
    print(f"Point P({x},{y}) is located in the CENTER of the coordinate system")
elif x > 0 and y > 0:
    print(f"Point P({x},{y}) is in the FIRST quadrant of the coordinate system")
elif x < 0 and y > 0:
    print(f"Point P({x},{y}) is in the SECOND quadrant of the coordinate system")
elif x < 0 and y < 0:
    print(f"Point P({x},{y}) is in the THIRD quadrant of the coordinate system")
elif x > 0 and y < 0:
    print(f"Point P({x},{y}) is in the FORTH quadrant of the coordinate system")

print()




def f(x, y):
    if x == 0 and y == 0:
        return f"Punkt P({x},{y}) znajduje się w CENTRUM układu współrzędnych"
    elif x > 0 and y > 0:
        return f"Punkt P({x},{y}) znajduje się w PIERWSZEJ ćwiartce układu współrzędnych"
    elif x < 0 and y > 0:
        return f"Punkt P({x},{y}) znajduje się w DRUGIEJ ćwiartce układu współrzędnych"
    elif x < 0 and y < 0:
        return f"Punkt P({x},{y}) znajduje się w TRZECIEJ ćwiartce układu współrzędnych"
    elif x > 0 and y < 0:
        return f"Punkt P({x},{y}) znajduje się w CZWARTEJ ćwiartce układu współrzędnych"
    


if __name__ == "__main__":
    print(f(7,5))