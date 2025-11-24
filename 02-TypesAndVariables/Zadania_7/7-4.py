#diameter - średnica
#circumference - obwód
#A tree can be cut down if its circumference is at least 50 cm.

tree = int(input("Enter tree circumference in cm: "))
diameter = tree / 3.14
cut_down = diameter >= 50

print(f'Tree diameter is: {diameter} cm')
print(f'Tree can be cut down: {cut_down}')