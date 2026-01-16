import re

file_name = "files.txt"

with open(file_name, 'r', encoding="utf-8") as file:
    content = file.read()

    pattern = r'\.[a-z]{4}$'

    match = re.findall(pattern, content, re.MULTILINE)
    print(match)