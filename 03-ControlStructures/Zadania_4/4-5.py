###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    # read the character's code (use ord())
    code = ord(char)
    # add one to the character's code
    code += 1
    # replace new character code with its
    # corresponding character (use chr())
    character = chr(code)
    # add encrypted character to encrypted text
    encrypted_text += character

print(plain_text)
print()
print(encrypted_text)
print()


def f(litera):
    wynik = ""
    for char in litera:
        kod = ord(char)
        kod += 1
        znak = chr(kod)
        wynik += znak
    return wynik

if __name__ == "__main__":
    print(f("a"))