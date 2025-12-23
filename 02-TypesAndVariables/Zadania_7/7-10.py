###
# A program that enables a user to challenge a computer.
# The computer throws dice. Then, the user then tries to guess
# the number from dice by entering a number from 1 to 6
# from the keyboard. If the user has guessed the number
# from the dice, the computer prints True. Otherwise,
# the computer prints False.
#
import random

computer = random.randint(1,6)
you = int(input("Guess the number: "))

result = you == computer

print(f"You won: {result}")
print(f"The random number was: {computer}")
print()





def f(number):
    comp = random.randint(1,6)
    print(comp)
    result = number == comp
    return result

if __name__ == "__main__":
    print(f(1))