###
# The car has three driving modes: Auto (A), Manual (M) and Eco (E).
# In each of these three modes, the average fuel consumption in liters
# per 100 km is 7, 9 and 6 respectively. Write a program that calculates
# total fuel consumption for a given distance in km and a given
# driving mode.
#
driving_mode = input('Enter driving mode (A/M/E): ')
distance = int(input('Enter distance in km: '))

if driving_mode == 'A':
    fuel_consumption = 7 # liters per 100km
elif driving_mode == 'M':
    fuel_consumption = 9
elif driving_mode == "E":
    fuel_consumption = 6
else:
    print("Incorrect driving mode")
total_consumption = distance / 100 * fuel_consumption

print(f'Total fuel consumption over a distance of {distance} km in driving mode {driving_mode} is {total_consumption} liters')
print()



def f(mode, distance):
    if mode == "A":
        fuel_consumption = 7
    elif mode == "M":
        fuel_consumption = 9
    elif mode == "E":
        fuel_consumption = 6
    else:
        return "Incorrect driving mode"
    total = fuel_consumption / 100 * distance
    return f'{total:.0f}'


if __name__ == "__main__":
    print(f("A", 400))