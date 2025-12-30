###
# Checking whether a car exceeded the speed limit
#

speed_limit = 140
car_speed = int(input('Enter car speed (km/h): '))

if car_speed > speed_limit:
    print(f'Your speed is {car_speed}km/h')
    print('Warning: speed limit exceeded!!')
    
print()


def f(speed):
    limit = 140
    if speed > limit:
        return "SUCCESS you exceeded speed limit!"
    else:
        return "Keep trying"
        


if __name__ == "__main__":
    print(f(330))