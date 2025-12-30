a = 0
b = 1

numbers = []
numbers.append(a)
numbers.append(b)

for i in range(1, 19):
    c = a + b
    numbers.append(c)
    a = b
    b = c

print(*numbers, end=" ")
print()
print()





def f():
    a = 0
    b = 1

    numbers = []
    numbers.append(a)
    numbers.append(b)

    for i in range(1,19):
        c = a + b
        numbers.append(c)
        a = b
        b = c
    return numbers

if __name__ == "__main__":
    print(*f())