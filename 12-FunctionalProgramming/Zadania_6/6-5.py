array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

filtered = list(filter(lambda x: x % 2 == 0 and x % 3 == 0, array))

print(f"Numbers divisible by 2 and 3 without remainder: ")
for number in filtered:
    print(number, end=", ")