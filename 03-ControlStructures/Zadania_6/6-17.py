time_24 = input("Enter time (24-hour format): ")

hour_str, minute_str = time_24.split(":")
hour = int(hour_str)
minute = int(minute_str)

if hour == 0:
    hour_12 = 12
    period = "am"
elif 1 <= hour <= 11:
    hour_12 = hour
    period = "am"
elif hour == 12:
    hour_12 = 12
    period = "pm"
else:
    hour_12 = hour - 12
    period = "pm"

print(f"Time in 12-hour format: {hour_12}:{minute_str}{period}")
print()





def f(time_24):
    hour_str, minute_str = time_24.split(":")
    hour_str = int(hour)
    minute_str = int(minute)

    if hour == 0:
        hour_12 = 12
        period = "am"
    elif 1 <= hour <= 11:
        hour_12 = hour
        period = "am"
    elif hour == 12:
        hour_12 = 12
        period = "pm"
    else:
        hour_12 = hour - 12
        period = "pm"
    return f"Time in 12-hour format: {hour_12}:{minute}{period}"


if __name__ == "__main__":
    print(f("16:32"))