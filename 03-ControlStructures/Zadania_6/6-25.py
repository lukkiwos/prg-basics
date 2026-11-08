liczba = "1"

for x in range(1,10):
    print(f"{x * liczba}")
    liczba = int(liczba)
    liczba += 1
    liczba = str(liczba)
print()



for y in range(1,10):
    print(str(y) * y)