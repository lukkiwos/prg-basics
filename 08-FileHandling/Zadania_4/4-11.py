file_name = input("Enter file name: ")

with open(file_name, 'w', encoding="utf-8") as file:
    
    for x in range(1, 101):
        second_power = x ** 2
        third_power = x ** 3

        line = f"{x}, {second_power}, {third_power}"
        print(line)

        file.write(line + '\n')
    
    
    