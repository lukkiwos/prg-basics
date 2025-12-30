
for i in range(1,6):
    result_1 = "*" * i
    print(result_1)

for x in range(4,0, -1):
    result_2 = "*" * x
    print(result_2)

print()
print()





def f():
    lines = []
    
    for i in range(1,6):
        lines.append(i * "*")
        
    for x in range(4,0, -1):
        lines.append(x * "*")
        
    return lines


if __name__ == "__main__":
    for line in f():
        print(line)