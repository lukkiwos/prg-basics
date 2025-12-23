###
# Write a program that calculates and prints
# the income of a family per person. To print the results
# in a readable form, use f-strings.
#

father_income = 5450
mother_income = 4920

family_members = 5
total_income = father_income + mother_income

income_per_person = total_income / family_members

print(f'Total family income is {total_income} zł, and income per person is {income_per_person:.2f} zł')
print()



def f(income1, income2, members):
    total_inc = income1 + income2
    inc_per_pers = total_inc / members
    return inc_per_pers

if __name__ == "__main__":
    print(f"Income per person is: {f(20000, 12137, 7):.2f} zł")