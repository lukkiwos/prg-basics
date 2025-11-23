###
# A program that, calculates distance to the horizon,
# d = 3.57 * √h
# where:
# d - distance to the horizon in kilometers
# h - height above sea level in meters
###

import math
h = float(input("Enter height above sea level in meters: "))
d = 3.57 * math.sqrt(h)
print("Distance to the horizon is: ", d, "kilometers")
