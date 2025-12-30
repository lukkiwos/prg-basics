import random

print("20 random numbers ranging from 5 to 10: ")

for i in range(1,21):           # for i in range(20)
    print(random.randint(5,10), end=" ")
print()
print()



def f():
    import random

    for i in range(20):
        print(random.randint(5,10), end=" ")



if __name__ == "__main__":
    print(f())