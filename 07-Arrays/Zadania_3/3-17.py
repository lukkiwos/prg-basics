my_tuple = (50, 20, 40, 50, 30, 50)

print("Tuple:", ", ".join(map(str, my_tuple)))

value = int(input("Value: "))

occurrences = 0

for x in my_tuple:
    if x == value:          # occurrences = my_tuple.count(value)
        occurrences += 1

print(f"Number of occurrences: {occurrences}")