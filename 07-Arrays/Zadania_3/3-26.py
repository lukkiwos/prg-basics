import matplotlib.pyplot as plt
import math

x = []
y = []

# create x values (angles in degrees)
for n in range(0, 361):  # od 0 do 360 stopni
    x.append(n)

# create y values
for angle in x:
    y.append(math.sin(math.radians(angle)))  # zamiana stopni na radiany

# print chart
plt.plot(x, y)
plt.title("Graph of y = sin(x)")
plt.xlabel("Angle (degrees)")
plt.ylabel("y = sin(x)")
plt.grid(True)
plt.show()