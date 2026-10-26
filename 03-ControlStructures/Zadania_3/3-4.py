###
# Checks whether at least one number entered
# from the keyboard is not negative
# 
x = int(input('Enter first number: '))
y = int(input("Enter second number: "))

if not x < 0 or not y < 0 :
    print(f'At least one of the numbers {x} and {y} is not negative')
print()



def f(a,b):
    if a > 0 or b > 0:
        return "Jedna z liczb na pewno jest dodatnia"
    else:
        return "Liczby są ujemne"


if __name__ == "__main__":
    print(f(1,2))
    print(f(-4,-6))
    