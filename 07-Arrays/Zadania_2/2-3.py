# Weekly expenses for different categories
# [Food, Transport, Utilities]

monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]


# Calculates expenses
# Use loop statements
total_by_category = [0, 0, 0]
total_by_week = []
total_month = 0

for week in monthly_expenses:
    week_sum = 0

    for i in range(len(week)):
        total_by_category[i] += week[i]
        week_sum += week[i]

    total_by_week.append(week_sum)
    total_month += week_sum


# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food: ',total_by_category[0])
print('Transport: ',total_by_category[1])
print('Utilities: ',total_by_category[2])

print("Total expenses by week: ")
print('Week 1: ',total_by_week[0])
print('Week 2: ',total_by_week[1])
print('Week 3: ',total_by_week[2])
print('Week 4: ',total_by_week[3])
print('---------------')
print('TOTAL: ',total_month)