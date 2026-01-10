names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

index = 0
longest_name = ""

while index < len(names):
    if len(names[index]) > len(longest_name):
        longest_name = names[index]
    
    index += 1

print("Names:",  ", ".join(names))
print(f"Longest name: {longest_name}")