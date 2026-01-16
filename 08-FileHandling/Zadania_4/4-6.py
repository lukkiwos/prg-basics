file_name = input("File name: ")

try:
    with open(file_name, 'r', encoding="utf-8") as file:
        content = file.read()

        lines = content.splitlines()
        line_count = len(lines)

        characters_count = len(content)

        words = content.split()
        word_count = len(words)


    print(f"Number of lines: {line_count}")
    print(f"Number of characters: {characters_count}")
    print(f"Number of words: {word_count}")


except FileNotFoundError:
    print(f"There is no file called {file_name}")