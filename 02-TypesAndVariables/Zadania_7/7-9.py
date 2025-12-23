import random

random_number = random.randint(1,6)
special_number = random_number == 1 or random_number == 6

print(f"Dice rolled: {random_number}")
print(f"Special number (1 or 6): {special_number}")
print()



def f():
    number = random.randint(1,6)
    print(number)
    special = number == 1 or number == 6
    return special

if __name__ == "__main__":
    print(f())