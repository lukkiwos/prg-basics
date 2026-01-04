def month(n):
    if n == 1:
        month = "January"
    elif n == 2:
        month = "February"
    elif n == 3:
        month = "March"
    elif n == 4:
        month = "April"
    elif n == 5:
        month = "May"
    elif n == 6:
        month = "June"
    elif n == 7:
        month = "July"
    elif n == 8:
        month = "August"
    elif n == 9:
        month = "September"
    elif n == 10:
        month = "October"
    elif n == 11:
        month = "November"
    elif n == 12:
        month = "December"
    else:
        return "Error"
    
    return f"The name of month {n} is: {month}"



if __name__ == "__main__":
    x = int(input("Enter month number: "))
    print(month(x))