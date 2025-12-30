###
# Checks whether at least one number entered
# from the keyboard is not negative
# 
x = int(input('Enter first number: '))
y = int(input("Enter second number: "))

if not x < 0 or not y < 0:
    print(f'At least one of the numbers {x} and {y} is not negative')

print()



def f(x, y):
    if not x < 0 or not y < 0:
        return f"Co najmniej jedna liczba z {x} i {y} nie jest ujemna"
    

if __name__ == "__main__":
    print(f(-1, 4))