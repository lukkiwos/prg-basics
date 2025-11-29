###
# Calculation of circle area and circumference 
#
import math

# determine radius and PI values
radius = float(input("Enter radius: "))

# calculate area
area = math.pi * (radius ** 2)

# calculate circumference
circumference = 2 * math.pi * radius

# print results
print(f'Circumference = {circumference:.2f}\n Area = {area:.2f}')
