###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
side_a = input('a = ')
side_b = input("b = ")
side_c = input("c = ")
a = int(side_a)
b = int(side_b)
c = int(side_c)

volume = a * b * c
area = 2 * (a*b + a*c + b*c)

print(f"Volume = {volume}, Surface area = {area}")
print()



def f(x, y, z):
    objetosc = x * y * z
    pole = 2 * (x*y + x*z + y*z)
    return objetosc, pole

if __name__ == "__main__":
    print(f(8, 1, 2))