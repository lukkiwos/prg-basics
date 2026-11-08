age = int(input("Enter your age: "))

if age > 64:
    print("Senior")
elif age > 19:
    print("Adult")
elif age > 12:
    print("Teen")
elif age > 0:
    print("Child")
print()


def f(wiek):
    if wiek > 64:
        return "Senior"
    elif wiek > 19:
        return "Adult"
    elif wiek > 12:
        return "Teen"
    elif wiek > 0:
        return "Child"



if __name__ == "__main__":
    print(f(65))
    print(f(64))
    print(f(20))
    print(f(19))
    print(f(13))
    print(f(12))
