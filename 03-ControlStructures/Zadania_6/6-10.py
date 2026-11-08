dog_age = int(input("Enter the dog's age in human years: "))

dog_years = (2 * 10.5) + (4 * (dog_age - 2))

print(f"The dog's age in dog's years is {dog_years:.0f} years.")
print()



def f(dog_age1):
    dog_years1 = (2 * 10.5) + (4 * (dog_age1 - 2))

    return dog_years1


if __name__ == "__main__":
    print(f(15))
