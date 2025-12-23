###
# A program that, for a given speed in km/h,
# prints the speed in m/s
#

speed_kmh = 70
speed_ms = speed_kmh / 3.6
print(f"{speed_kmh} km/h = {speed_ms:.2f} m/s ")




def f(kmh):
    ms = kmh / 3.6
    return ms

if __name__ == "__main__":
    print(f"{f(36)} m/s")