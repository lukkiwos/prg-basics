###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#

import math

def triangle_area(a,b,c):
    p = (a + b + c) / 2
    area = int(math.sqrt(p*(p-a)*(p-b)*(p-c)))
    return area


a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))

area_result = triangle_area(a,b,c)

print(f'\n The area of a triangle with sides ({a}, {b}, {c}) is: {area_result}')
