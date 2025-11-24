#Write a program that prints a numerical representation of each letter of your name.

name = input("Enter your name: ")
name = len(name)
print(f'My name has {name} letters')

name = 'Lukasz'
print(f'My name is {name}')

print(f'The letter {name[0]} has a code {ord(name[0])}')
print(f'The letter {name[1]} has a code {ord(name[1])}')
print(f'The letter {name[2]} has a code {ord(name[2])}')
print(f'The letter {name[3]} has a code {ord(name[3])}')
print(f'The letter {name[4]} has a code {ord(name[4])}')
print(f'The letter {name[5]} has a code {ord(name[5])}')
