categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

max_expense = expenses[0]
index = 1
count = 0

while count < len(expenses):
    if expenses[count] > max_expense:
        max_expense = expenses[count]
        index = count
    count += 1

category = categories[index]

print(f"{category} is {max_expense}")