###
# A program that calculates the length of the diagonal
# of a rectangle with sides a and b.
#
import math
a = 5
b = 8
diagonal = math.sqrt((a ** 2) + (b ** 2))
print(f"{diagonal:.2f}")



def f(x, y):
    result = math.sqrt((x ** 2) + (y ** 2))
    return result

if __name__ == "__main__":
    print(f"Diagonal is: {f(15, 8):.2f}")