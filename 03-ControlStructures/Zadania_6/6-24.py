symbol = "*"
liczba = 1

for x in range(1,6):
    print(liczba * symbol)
    liczba += 1
liczba -= 1
for x in range(1,5):
    liczba -= 1
    print(liczba * symbol)
print()


for y in range(1,6):
    print(y * symbol)
for y in range(4,0,-1):
    print(y * symbol)