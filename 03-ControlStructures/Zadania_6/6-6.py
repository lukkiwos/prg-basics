number_of_hours = int(input("Enter number of hours of parking: "))

if number_of_hours > 6:
    print("60 PLN")
elif number_of_hours > 2:
    print("15 PLN")
elif number_of_hours > 0:
    print("5 PLN")
print()


def f(hours):
    if hours > 6:
        return "60 PLN"
    elif hours > 2:
        return "15 PLN"
    elif hours > 0:
        return "5 PLN"


if __name__ == "__main__":
    print(f(7))
    print(f(6))
    print(f(3))
    print(f(2))
    print(f(1))