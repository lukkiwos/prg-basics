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

total_consumption = (fuel_consumption * distance) / 100
print(f'Total fuel consumption over a distance of {distance} km in driving mode {driving_mode} is {total_consumption:.0f} liters')
print()



def f(mode, dist):
    if mode == "A":
        consumption = 7
    elif mode == "M":
        consumption = 9
    elif mode == "E":
        consumption = 6

    total = (consumption * dist) / 100

    return f"Całkowite zuzycie paliwa na dystansie {dist} km w trybie jazdy {mode} jest równe {total:.0f} litrów"


if __name__ == "__main__":
    print(f("M", 200))
    print(f("A", 400))
    print(f("E", 350))