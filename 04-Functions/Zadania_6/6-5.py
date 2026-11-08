def f(number, x, y):
    if number >= x and number <= y:
        return True
    else:
        return False


if __name__ == "__main__":
    number = int(input("A number: "))
    x = int(input("x = "))
    y = int(input("y = "))

    if f(number,x,y):
        message = "Yes"
    else:
        message = "No"
    print(f"Number {number} in the range <{x},{y}>: {message}")