store = {
    'Laptop': 15,
    'Desktop PC': 10,
    'Monitor': 25,
    'Keyboard': 50,
    'Mouse': 60,
    'External Hard Drive': 30,
    'Printer': 12,
    'Router': 20,
    'USB Flash Drive': 100,
    'Graphics Card': 8
}

suma = 0

for key, value in store.items():
    print(f"{key} : {value}")
    suma += value


print()
print(f'The total number of products in the store: {suma}')