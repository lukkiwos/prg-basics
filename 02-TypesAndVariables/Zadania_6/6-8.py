###
# A program that calculates
# how many letters are between two given letters
#

first = input('Enter first letter: ')
last = input('Enter last letter: ')

print()
first_letter_code = ord(first)
print(f"The first letter code is: {first_letter_code}")

last_letter_code = ord(last)
print(f"The last letter code is: {last_letter_code}")
print()

if first == last:
    number_of_letters = last_letter_code - first_letter_code
else:
    number_of_letters = last_letter_code - first_letter_code - 1

print(f'Between {first} and {last} is: {number_of_letters} letters')
print()


def f(letter1, letter2):
    code1 = ord(letter1)
    code2 = ord(letter2)
    if letter1 == letter2:
        number = code2 - code1
    else:
        number = code2 - code1 - 1
    return number

if __name__ == "__main__":
    result = f("B", "M")
    print(f"The result is: {result} letters")