###
# Calculates the sum of integer numbers in the range <1,5>
#
sum = 0 

for i in range(5,11):
    sum += i

print(f'Sum is {sum}')



def f(x, y):
    suma = 0
    for i in range(x,y):
        suma += i
    return f"Suma to: {suma}"


if __name__ == "__main__":
    print(f(1, 6))