###
# Checking if both people are adults
#
person1_name = input('Enter first person name: ')
person1_age = int(input('Enter first person age: '))

person2_name = input("Enter second person name: ")
person2_age = int(input("Enter second person age: "))

if person1_age >= 18 and person2_age >= 18:
    print(f'Both {person1_name} and {person2_name} are adults.')
else:
    print(f'Either {person1_name} or {person2_name} is not an adult.')

print()





def f(name_1, age_1, name_2, age_2):
    if age_1 >= 18 and age_2 >= 18:
        return f"Both {name_1} and {name_2} are adults"
    else:
        return f"Either {name_1} or {name_2} is NOT an adult"
    


if __name__ == "__main__":
    print(f("Łukasz", 19, "Karolina", 18))