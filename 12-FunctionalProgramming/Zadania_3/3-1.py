transactions_in_eur = [15.90, 38.47, 4.07, 132.70, 9.15]

transactions_in_pln = list(map(lambda x: x * 4.5, transactions_in_eur))

print("Transactions in EURO:")
for euro in transactions_in_eur:
    print(f"{euro:.2f}")

print()
print()

print("Transactions in PLN:")
for pln in transactions_in_pln:
    print(f"{pln:.2f}")