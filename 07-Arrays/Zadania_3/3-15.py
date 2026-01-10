my_tuple = (10, 20, 30, 40, 50)

reverse_list = []

index = len(my_tuple) - 1

for x in my_tuple:
    reverse_list.append(my_tuple[index])
    index -= 1

print(f"Tuple: {my_tuple}")
print(f"Reverse order: {reverse_list}")