###
# Checking whether a car exceeded the speed limit
#
speed_limit = 140
car_speed = int(input('Enter car speed (km/h): '))

if car_speed <= speed_limit:
    print(f'Your speed is {...}km/h')
else:
    print('Warning: Great you exceeded the speed limit!!')