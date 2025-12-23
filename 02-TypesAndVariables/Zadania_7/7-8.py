###
# A program that prints results of three dice rolls
# and the sum of dice rolled.
#
import random

dice_roll1 = random.randint(1,6)
dice_roll2 = random.randint(1,6)
dice_roll3 = random.randint(1,6)

total = dice_roll1 + dice_roll2 + dice_roll3

print(dice_roll1)
print(dice_roll2)
print(dice_roll3)
print()
print(f"The sum of dice rolled is: {total}")