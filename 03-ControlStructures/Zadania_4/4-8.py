###
# Calculates values for the following fractions: 1/2, 1/3, ..., 1/10
#
for i in range(1,11):
    print(f'1/{i} = {1/i}')
print()


def f(x, y):
    for i in range(x, y):
        print(f"1/{i} = {1/i}")
    return "Done"


if __name__ == "__main__":
    print(f(1, 21))