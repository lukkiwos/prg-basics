###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    # read the character's code (use ord())
    x = ord(char)
    
    # add one to the character's code
    y = x + 1
    
    # replace new character code with its
    # corresponding character (use chr())
    z = chr(y)
    
    # add encrypted character to encrypted text
    encrypted_text = encrypted_text + z 

print(plain_text)
print(encrypted_text)
print()



def f(text):
    encrypted_text = ""
    for char in text:
        x = ord(char)
        y = x + 1
        z = chr(y)
        encrypted_text = encrypted_text + z
    return encrypted_text


if __name__ == "__main__":
    print(f("Blablabla i dont like the juice"))