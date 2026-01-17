countries = [
{"name": "Poland ", "population": 38000000},
{"name": "Germany", "population": 84000000},
{"name": "France ", "population": 69000000},
{"name": "USA    ", "population": 340000000},
{"name": "Russia ", "population": 144000000}
]

print("COUNTRY    POPULATION")

for country in countries:
    print(country["name"], "  ", country["population"])    
