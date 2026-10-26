###
# Calculates the sum of integer numbers in the range <1,5>
#
sum = 0

for i in range(5,11):
    sum += i

print(f'Sum is {sum}')
print()


def f(a,b):
    suma = 0
    for i in range(a,b + 1):
        suma += i

    return suma


if __name__ == "__main__":
    print(f(1,5))
    print(f(5,10))