###
# Printing student's personal data
#
name = "Adam"
print(f"My name is {name}.")
print()

age = 19
height = 180
x = 6
next_age = age + x

print(f"My name is {name}")
print(f"I am {age} years old, and my height is {height} cm.")
print(f"In {x} years I will be {next_age} years old.")
print()




def f(imie, wiek, wzrost, y):
    wiek2 = wiek + y
    print(f"My name is {imie}")
    print(f"I am {wiek} years old, and my height is {wzrost} cm.")
    print(f"In {y} years I will be {wiek2} years old.")
    return ""

if __name__ == "__main__":
    print(f("Łukasz", 19, 180, 11))