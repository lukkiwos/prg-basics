###
# Checking whether a car exceeded the speed limit
#
speed_limit = 140
car_speed = int(input('Enter car speed (km/h): ') )

if car_speed > speed_limit:
    print(f'Your speed is {car_speed}km/h')
    print('Warning: speed limit exceeded!!')


def f(speed):
    limit = 140
    if speed > limit:
        return f"You exceeded speed limit. Your speed: {speed}km/h"

if __name__ == "__main__":
    print(f(150))