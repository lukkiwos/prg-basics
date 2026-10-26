###
# Calculates the sum of even numbers in the range <1,10>
#
sum = 0

for i in range(1,11):
    if not i % 2 == 0:
        continue
    sum += i

print(f'Sum of even numbers in the range <1,10> is {sum}')
print()


def f(a,b):
    suma = 0
    for i in range(a,b + 1):
        if i % 2 == 0:
            suma += i
        else:
            suma = suma

    return suma


if __name__ == "__main__":
    print(f(1,10))
