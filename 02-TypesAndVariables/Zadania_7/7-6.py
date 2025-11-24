#Enter vehicle speed: 158
#Speed is valid: False

vehicle_speed = int(input("Enter vehicle speed: "))
speed_valid = vehicle_speed > 40 and vehicle_speed < 140

print(f'Speed is valid: {speed_valid}')