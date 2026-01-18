import matplotlib.pyplot as plt

# data
temperature = {
    "Krakow": 7,
    "Warszawa": -2,
    "Sopot": 4,
    "Koszalin": -1,
    "Opole": 3
}

# use map() to create data arrays
cities = list(map(lambda item: item[0], temperature.items()))
temps = list(map(lambda item: item[1], temperature.items()))

# create bar chart
plt.figure()
plt.bar(cities, temps)
plt.title("Recorded Temperatures in Cities")
plt.xlabel("City")
plt.ylabel("Temperature (°C)")

plt.show()