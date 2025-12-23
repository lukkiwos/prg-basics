###
# Calculation of circle area and circumference 
#

import math

# determine radius and PI values
PI = 3.14
radius = int(input("Enter radius: "))

# calculate area 
area = PI * radius ** 2

# calculate circumference 
circumference = 2 * PI * radius

# print results
print(f"Circumference is: {circumference:.2f}")
print(f"Area is: {area:.2f}")
print()



def f(promien):
    obwod = 2 * PI * promien
    pole = PI * promien ** 2
    return obwod, pole


if __name__ == "__main__":
    print(f(3))