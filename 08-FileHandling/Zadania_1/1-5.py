count = 1

with open('countries.txt', 'r') as file:
    
    for line in file:
        x = str(count) + ". " + line
        print(x, end="")
        count += 1