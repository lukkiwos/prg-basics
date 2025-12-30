# while condition:
    # code block to execute

count = 0
while count < 5:
    print(count)
    count += 1
print()



def f(x):
    count = 0
    while count < x:
        print(count)
        count += 1
    return "Done"


if __name__ == "__main__":
    print(f(10))