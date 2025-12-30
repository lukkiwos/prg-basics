for a in range(1,8):
    print(a, end=" ")
    for b in range(7,8):
        print(f'{a+b}', end=" ")
        for c in range(7,8):
            print(f"{a+b+c}", end=" ")
            for d in range(7,8):
                print(f"{a+b+c+d}", end=" ")
                for e in range(7,8):
                    print(f"{a+b+c+d+e}", end=" ")
                    for f in range(7,8):
                        print(f"{a+b+c+d+e+f}", end=" ")
                        for g in range(7,8):
                            print(f"{a+b+c+d+e+f+g}")


print()
print()

for x in range(1,8):
    for y in range(0,7):
        print(f"{x+y * 7}", end=" ")
    print()
    