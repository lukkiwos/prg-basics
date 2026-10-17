###
# Calculation of circle area and circumference 
#
import math
# determine radius and PI values
r = int(input("Enter radius of a circle: "))
pi = 3.14

# calculate area 
area = pi * (r ** 2)

# calculate circumference 
circumference = pi * (2 * r)

# print results
print(f"Circumference = {circumference:.2f}")
print(f"Area = {area:.2f}")