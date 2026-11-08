###
# Counts vowels in the text
#
text = "This is a sample text."
vowels = "aeiouAEIOU"
vowel_count = 0
count = 0

# Count vowels in the text # 6
while count < len(text):
    if text[count] in vowels:
        vowel_count += 1
    count += 1

print(f"The number of vowels in the text is: {vowel_count}")
print()



# for char in text:
    # if char in vowels:
        # vowel_count += 1



def f(txt):
    count = 0
    vowels_count = 0
    vowelss = "aeiouAEIOU"
    while count < len(txt):
        if txt[count] in vowelss:
            vowels_count += 1
        count += 1
    return vowels_count


if __name__ == "__main__":
    print(f("This is a sample text.e"))