temperature = {
    "Krakow": 7,
    "Warszawa": -2,
    "Sopot": 4,
    "Koszalin": -1,
    "Opole": 3
}


positive_temp = list(map(lambda value: value[0], filter(lambda value: value[1] > 0, temperature.items())))
    
print(f"Cities with positive temperatures: {', '.join(map(str, positive_temp))}")