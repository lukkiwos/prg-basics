#Write a program that calculates a dog's age in dog's years. 
# For the first two years, a dog's life is equal to 10.5 human years. 
# After that, each dog year is equal to 4 human years.

age_in_human_years = int(input("Enter the dog's age in human years: "))

dog_age = 0.0

if age_in_human_years <= 0:
    dog_age = 0.0
    print("Invalid age entered")

elif age_in_human_years <= 2:
    dog_age = age_in_human_years * 10.5

else:
    dog_age = 2 * 10.5
    remaining_years = age_in_human_years - 2
    dog_age += remaining_years * 4


print(f"The dog's age in dog's years is: {int(dog_age)} years.")