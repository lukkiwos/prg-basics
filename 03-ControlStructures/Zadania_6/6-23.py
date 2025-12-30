number = int(input("Enter number: "))

for i in range(1,11):
    print(f"{number} * {i} = {number * i}")

print()
print()




def f(number):
    result = []
    
    for i in range(1,11):
        result.append(f"{number} * {i} = {number * i}")
    
    return result


if __name__ == "__main__":
    for line in f(4):
        print(line)