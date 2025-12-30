age = int(input("Enter your age: "))

if age > 64:
    print(f"Senior: 65 or older")
elif age > 19:
    print(f"Adult: 20 to 64")
elif age > 12:
    print(f"Teen: 13 to 19")
elif age > 0:
    print(f"Child: under 13")

print()





def f(age):
    if age > 64:
        return "Senior: 65 or older"
    elif age > 19:
        return "Adult: 20 to 64"
    elif age > 12:
        return "Teen: 13 to 19"
    elif age > 0:
        return "Child: under 13"
    


if __name__ == "__main__":
    print(f(14))