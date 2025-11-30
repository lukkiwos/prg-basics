###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#

plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    # read the character's code (use ord())
    character_code = ord(char)

    # add one to the character's code
    character_code += 1                     # zamiast character_code = character_code + 1

    # replace new character code with its
    # corresponding character (use chr())
    new_character = chr(character_code)

    # add encrypted character to encrypted text
    encrypted_text += new_character

print(plain_text)
print(encrypted_text)