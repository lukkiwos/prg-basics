
circumference = int(input("Enter tree circumference in cm: "))
diameter = circumference / 3.14 >= 50

print(f"Tree can be cut down: {diameter}")
print()


def f(circumference):
    diameter = circumference / 3.14 >= 50
    return diameter

if __name__ == "__main__":
    print(f(160))
    print(f(90))
    print(f(230))
    print(f(120))