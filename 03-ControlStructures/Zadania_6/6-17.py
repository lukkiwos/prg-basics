time_24 = input("Enter time (24-hour format): ")
time_12 = ""
am_or_pm = ""

if int(time_24[0:2]) == 0:
    time_12 = f"12{time_24[2:]}"
    am_or_pm = "am"
elif int(time_24[0:2]) >= 1 and int(time_24[0:2]) <= 11:
    time_2 = int(time_24[0:2])
    time_2 = str(time_2)
    time_12 = f"{time_2}{time_24[2:]}"
    am_or_pm = "am"
elif int(time_24[0:2]) == 12:
    time_12 = f"{time_24}"
    am_or_pm = "pm"
elif int(time_24[0:2]) >= 13 and int(time_24[0:2]) <= 23:
    time = int(time_24[0:2])
    time -= 12
    time = str(time)
    time_12 = f"{time}{time_24[2:]}"
    am_or_pm = "pm"


print(f"Time in 12-hour format: {time_12}{am_or_pm}")
print()



def f(t_24):
    t_12 = ""
    pm_or_am = ""

    if int(t_24[0:2]) == 0:
        t_12 = f"12{t_24[2:]}"
        pm_or_am = "am"
    elif int(t_24[0:2]) >= 1 and int(t_24[0:2]) <= 11:
        t_2 = int(t_24[0:2])
        t_2 = str(t_2)
        t_12 = f"{t_2}{t_24[2:]}"
        pm_or_am = "am"
    elif int(t_24[0:2]) == 12:
        t_12 = f"{t_24}"
        pm_or_am = "pm"
    elif int(t_24[0:2]) >= 13 and int(t_24[0:2]) <= 23:
        t = int(t_24[0:2])
        t -= 12
        t = str(t)
        t_12 = f"{t}{t_24[2:]}"
        pm_or_am = "pm"

    return f"{t_12} {pm_or_am}"


if __name__ == "__main__":
    print(f("00:15"))
    print(f("08:30"))
    print(f("12:00"))
    print(f("15:00"))
    print(f("20:45"))