def month(n):
    if n == 1:
        return "January"
    elif n == 2:
        return "February"
    elif n == 3:
        return "March"
    elif n == 4:
        return "April"
    elif n == 5:
        return "May"
    elif n == 6:
        return "June"
    elif n == 7:
        return "July"
    elif n == 8:
        return "August"
    elif n == 9:
        return "September"
    elif n == 10:
        return "October"
    elif n == 11:
        return "November"
    elif n == 12:
        return "December"


if __name__ == "__main__":
    number = int(input("Enter month number: "))
    print(f"The name of month {number} is: {month(number)}")