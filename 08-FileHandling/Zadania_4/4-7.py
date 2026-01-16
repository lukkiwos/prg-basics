import re

text = input("Enter text: ")
vowels_pattern = r'[aeiouAEIOU]'

match = re.findall(vowels_pattern, text)
count = len(match)


print(f"Number of vowels in the text: {count}")