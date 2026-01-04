def f(number, x, y):
    if x <= number <= y:
        result = "Yes"
    else:
        result = "No"

    return f"Number {number} in the range <{x},{y}>: {result}"




if __name__ == "__main__":
    print(f(7, 2, 15))