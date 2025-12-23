integer_number = int(input("Enter number: "))

binary_number = bin(integer_number)
hexadecimal_number = hex(integer_number)

print(f"Binary number: {binary_number}")
print(f"Hexadecimal number: {hexadecimal_number}")
print()


def f(number):
    binary = bin(number)
    hexadecimal = hex(number)
    return binary, hexadecimal


if __name__ == "__main__":
    print(f(125))