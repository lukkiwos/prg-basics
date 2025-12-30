for i in range(6,-1,-3):
    for j in range(1,4):
        print(f'{i+j}',end=' ')
    print()

print()
print()



i = 6
while i >= 0:
    j = 1
    while j <= 3:
        print(f"{j+i}", end=" ")
        j += 1
    print()
    i -= 3

print()
print()





def f():
    i = 6
    while i >= 0:
        j = 1
        while j <= 3:
            print(f"{i + j}", end = " ")
            j += 1
        print()
        i -= 3


if __name__ == "__main__":
    print(f())