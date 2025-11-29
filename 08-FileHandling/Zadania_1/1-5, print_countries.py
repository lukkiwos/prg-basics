###
# Reads from file, line by line
#
with open('countries.txt', 'r') as file:
    for line in file:
        print(line, end="")
        numbers = ["1", "2", "3", "4", "5"]
        for number in numbers:
            print(number, end="")