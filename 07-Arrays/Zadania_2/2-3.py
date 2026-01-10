# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# 1
category_totals = [0, 0, 0]

for week in monthly_expenses:
    for i in range(len(week)):
        category_totals[i] += week[i]

# 2
week_totals = [0, 0, 0, 0]
week_index = 0

for week in monthly_expenses:
    for expense in week:
        week_totals[week_index] += expense
    week_index += 1

# 3
total_expense = 0

for week in monthly_expenses:
    for expense in week:
        total_expense += expense
    


# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:', category_totals[0])
print('Transport:', category_totals[1])
print('Utilities:', category_totals[2])
print('Week 1:', week_totals[0])
print('Week 2:', week_totals[1])
print('Week 3:', week_totals[2])
print('Week 4:', week_totals[3])
print('---------------')
print('TOTAL:', total_expense)