###
# A program that prints your height both in cm and in feet and inches.
#
import math 

cm = 170
feet = cm / 30.48
inches = cm / 2.54

# calculate the number of feet --     1 foot == 12 inches
full_feets = int(inches // 12)
remaining_inches = math.ceil(inches % 12)


print()
print(f'I am {cm}cm tall, {full_feets} feet and {remaining_inches} inches')
print()



def f(cm):
    inch = cm / 2.54
    
    full_feet = int(inch // 12)
    remain_inch = math.ceil(inch % 12)
    
    return cm, full_feet, remain_inch

if __name__ == "__main__":
    print(f(170))