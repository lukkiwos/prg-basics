###
# A program that prints your height both in cm and in feet and inches.
#
import math

cm = 180

total_inches = cm / 2.54
inches = total_inches % 12
feet = int(total_inches // 12)

# calculate the number of feet


print(f'I am {cm}cm tall, i.e. {feet} feet and {inches:.2f} inches')