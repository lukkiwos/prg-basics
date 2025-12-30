car_speed = int(input("Enter car speed: "))

speed_limi_min = 40
speed_limi_max = 140

if car_speed < speed_limi_min or car_speed > speed_limi_max:
    print(f"Warning: invalid car speed!!! Your speed: {car_speed} km/h")
else:
    print(f"Your speed is valid")

print()




def f(car_speed):
    speed_limi_min = 40
    speed_limi_max = 140

    if car_speed < speed_limi_min or car_speed > speed_limi_max:
        return f"Warning: invalid car speed!!! Speed: {car_speed}"
    else:
        return f"Valid speed: {car_speed}"
    


if __name__ == "__main__":
    print(f(38))