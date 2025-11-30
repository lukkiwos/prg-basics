car_speed = int(input("Enter car speed: "))

speed_limit_min = 40
speed_limit_max = 140

if car_speed < speed_limit_min:
    print("Warning: low speed!!")

elif car_speed > speed_limit_max:
    print("Warning: high speed!!")

else:
    print("Apropriate speed")