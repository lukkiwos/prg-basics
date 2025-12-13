def is_in_range(number, x, y):
    return x <= number <= y

if __name__ == "__main__":
    print(f"Number 7 in the range <2,15>: {is_in_range(7, 2, 15)}")