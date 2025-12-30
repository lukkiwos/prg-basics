###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#
basic_salary = 5000
total_salary = 0
bonus = 0.30 # 30%
is_bonus = input('Does the employee receive a bonus? (Y/N): ') == 'Y'
print()

if is_bonus:
    total_salary = (basic_salary * bonus) + basic_salary
else:
    total_salary = basic_salary

print(f'Basic salary: {basic_salary}')
print(f'Bonus included? {is_bonus}')
print(f'Total salary: {total_salary}')
print()



def f(is_bonus):
    basic = 1000
    total = 0
    bonus = 0.5
    if is_bonus == "Y":
        total = basic * bonus + basic
    else:
        total = basic
    return total
    

if __name__ == "__main__":
    print(f("Y"))