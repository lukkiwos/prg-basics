a = 0
b = 1
c = 0

for x in range(20):
    print(a, end=" ")
    c = b
    b = a + b
    a = c
