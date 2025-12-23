# d = 3.57 * sqrt(h)
import math

height = float(input("Enter height in meters: "))
distance = 3.57 * math.sqrt(height)

print(f"Your distance for given height ({height} m) is: {distance:.2f} km")



def f(wysokosc):
    dystans = 3.57 * math.sqrt(wysokosc)
    return dystans

if __name__ == "__main__":
    print(f"Your distance to the horizon is: {f(35):.2f} km")