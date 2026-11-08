###
# Program that simulates the operation of an electronic thermometer.
#
temperature = 32

if temperature > 35:
    print("It is extermely hot")
elif temperature > 30:
    print("It is hot")
elif temperature >= 15:
    print("It is warm")
elif temperature >= 0:
    print("It is cold")
elif temperature < 0:
    print("Warning, frost")
print()


def f(temp):
    if temp > 35:
        return "It is extremely hot"
    elif temp > 30:
        return "It is hot"
    elif temp >= 15:
        return "It is warm"
    elif temp >= 0:
        return "It is cold"
    elif temp < 0:
        return "Warning, frost"


if __name__ == "__main__":
    print(f(33))
    print(f(30))
    print(f(8))
    print(f(0))
    print(f(-2))
