#Most female names in Polish end with the letter "a". 
# Write a program that prints the name entered from the keyboard, 
# provided it is a female name.

name = (input("Enter your name: "))

if name [-1] == "a":
    print(f"{name} -- Polish female name")

else:
    print(f"{name} -- is NOT a Polish female name")