def f(name):
    with open(name, 'r') as file:
        content = file.read()
        return content
    
file_content = f('pets.txt')

if file_content:
    word_list = file_content.split()        
    number_of_words = len(word_list)

    print(f"Number of words in 'pets.txt' file is: {number_of_words}")
