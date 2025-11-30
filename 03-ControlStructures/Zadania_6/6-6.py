#Write a program that asks for the number of hours of parking,
# then calculates and prints the correct fee.

hours = int(input("Type number of hours: "))

if hours >= 1 and hours <= 2:
    print("1-2 hours: 5 PLN")

elif hours >= 3 and hours <= 6:
    print("3-6 hours: 15 PLN")

elif hours > 6:
    print("Over 6 hours: 20 PLN")

else:
    print("You typed incorrect number of hours")