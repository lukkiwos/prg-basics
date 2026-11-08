car_speed = int(input("Enter car speed: "))

speed_limit_min = 40
speed_limit_max = 140

if car_speed < speed_limit_min or car_speed > speed_limit_max:
    print("Warning: invalid car speed!")
else:
    print("Valid car speed")
print()


def f(speed):
    min_speed = 40
    max_speed = 140

    if speed < min_speed or speed > max_speed:
        return False
    else:
        return True


if __name__ == "__main__":
    print(f(38))
    print(f(141))
    print(f(80))