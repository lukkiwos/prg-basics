###
# Prints a greeting
#
name = ''

while name == '':
    name = input('Enter your name: ')

print(f'Hello {name}')
print()


def f():
    name = ""
    while name == "":
        name = input("Enter your name: ")
    return f"Hello {name}"


if __name__ == "__main__":
    print(f())