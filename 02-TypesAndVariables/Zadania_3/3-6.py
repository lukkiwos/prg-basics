import math
height = float(input("Enter your height in meters: "))

distance = 3.57 * math.sqrt(height)

print(f"Your distance to the horizon is: {distance:.2f} km")