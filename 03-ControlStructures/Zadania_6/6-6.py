number_hours = int(input("Enter the number of hours of parking: "))
fee = 0

if number_hours > 6:
    fee = 20
    print(f"Over 6 hours: {fee} PLN")
elif number_hours >= 3:
    fee = 15
    print(f"3-6 hours: {fee} PLN")
elif number_hours <= 2:
    fee = 5
    print(f"1-2 hours: {fee} PLN")

print()





def f(hours):
    fee = 0
    if hours > 6:
        fee = 20
        return f"Over 6 hours: {fee} PLN"
    elif hours > 2:
        fee = 15
        return f"3-6 hours: {fee} PLN"
    elif hours > 0:
        fee = 5
        return f"1-2 hours: {fee} PLN"
    


if __name__ == "__main__":
    print(f(2))