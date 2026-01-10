array = [2.5, 7.1, 3.0, 10.2]

number = float(input("Enter number: "))

count = 0

for x in array:
    if x > number:
        count += 1

print(f"Number of elements greater than {number:.0f} is: {count}")