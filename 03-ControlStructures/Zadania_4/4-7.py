###
# Calculates the sum of even numbers in the range <1,10>
#
sum = 0

for i in range(1,11):
    if not i % 2 == 0:           # if i % 2 != 0
        continue
    sum += i

print(f'Sum of even numbers in the range <1,10> is: {sum}')
print()



def f(x, y):
    suma = 0
    for i in range(x, y):
        if i % 2 != 0:
            continue
        suma += i
    return f"Suma parzystych liczb w przedziale <{x},{y-1}> to: {suma}"



if __name__ == "__main__":
    print(f(1,21))