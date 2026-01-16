def read_from_file(name):
    with open(name) as file:
        content = file.read()
        return content
    

file_content = read_from_file('pets.txt')

file_lines = file_content.split()


x = len(file_lines)



print(file_content)
print()
print(f"Number of words in the text: {x}")