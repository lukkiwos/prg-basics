###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
def triangle_area(a,b,c):
    import math 

    s = (a + b + c) / 2
    result = math.sqrt(s*(s-a)*(s-b)*(s-c))
    
    return result



if __name__ == "__main__":
    x = triangle_area(3,4,5)
    print(f'The area of a triangle with sides 3, 4, 5 is: {x:.0f}')
    print()
    
    y = triangle_area(5,12,13)
    print(f'The area of a triangle with sides 5, 12, 13 is: {y:.0f}')
    print()

    z = triangle_area(7,24,25)
    print(f'The area of a triangle with sides 7, 24, 25 is: {z:.0f}')
    print()