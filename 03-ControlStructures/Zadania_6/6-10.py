human_years = int(input("Enter the dog's age in human years: "))

dogs_age = 0


if human_years <= 2:
    dogs_age = human_years * 10.5

if human_years > 2:
    human_years -= 2
    dogs_age = 21 + human_years * 4

print(f"The dog's age in dog's years is: {dogs_age:.0f} years.")