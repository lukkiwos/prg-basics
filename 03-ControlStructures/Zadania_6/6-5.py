###
# Program that simulates the operation of an electronic thermometer.
#
temperature = 32
if temperature > 35:
    print("It is extremely hot")
elif temperature > 30:
    print("It is hot")
elif temperature >= 15:
    print("It is warm")
elif temperature >= 0:
    print("It is cold")
elif temperature < 0:
    print("Warning, frost")

print()




def f(temperature):
    if temperature > 35:
        return "Jest w chuj gorąco"
    elif temperature > 25:
        return "Jest gorąco"
    elif temperature >= 15:
        return "Jest przyjemnie"
    elif temperature >= 0:
        return "Jest zimno"
    elif temperature < 0:
        return "Bardzo zimno"
    


if __name__ == "__main__":
    print(f(16))