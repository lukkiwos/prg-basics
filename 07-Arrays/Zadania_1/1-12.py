categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]


max_expense = max(expenses)

max_expense_index = expenses.index(max_expense)

most_expensive_category = categories[max_expense_index]


print()
print(f"Lista kategorii: {categories}")
print(f"Lista wydatków: {expenses}")
print()
print(f"Największy wydatek to: {max_expense}")
print(f"Najdroższa kategoria to: {most_expensive_category}")
print()