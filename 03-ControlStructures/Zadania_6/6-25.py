for i in range(1, 10):
    x = i * str(i)
    print(x)

print()
print()




def f():
    lines = []
    
    for i in range(1,10):
        lines.append(i * str(i))
    return lines


if __name__ == "__main__":
    for line in f():
        print(line)