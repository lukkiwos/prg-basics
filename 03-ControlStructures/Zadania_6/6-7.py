#Write a program that asks the user for their age 
# and then checks which age group they belong to.

age = int(input("Type your age: "))

if age < 13 and age > 0:
    print("Child")

elif age >= 13 and age <= 19:
    print("Teen")

elif age >= 20 and age <= 64:
    print("Adult")

elif age >= 65:
    print("Senior")

else:
    print("You typed wrong age number")