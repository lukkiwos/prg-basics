array = [
    ("Smith", "Lucy"),
    ("Jones", "Janet"),
    ("Lee", "Jerry"),
    ("Jackson", "Peter"),
    ("Johnson", "Rick"),
    ("Lewis", "Terry"),
    ("Clarke", "Robin")
]

for name, surname in array:
    print(name, surname)

print()


capital = list(map(lambda name: f"{name[0].upper()}, {name[1]}", array))

for name in capital:
    print(name)