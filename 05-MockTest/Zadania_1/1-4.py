sentence = "hello universe"
vowels = "aeiou"
count = 0

for char in sentence:
    if char in vowels:
        count += 1

print("Vowel count:", count)  # Output is incorrect