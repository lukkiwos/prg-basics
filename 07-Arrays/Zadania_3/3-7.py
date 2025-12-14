names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

separator = "    "
print(f"\nNames:  {separator.join(names)}\n")

longest_name = names[0]
maximum_length = len(longest_name)

for name in names:
    length= len(name)
    if length > maximum_length:
        longest_name = name
        maximum_length = length

print(f"Longest name: {longest_name}\n")