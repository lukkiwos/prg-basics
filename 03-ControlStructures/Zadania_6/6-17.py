time_24_hour_format = input("Enter time (24-hour format '00:00'): ")
pm_am = ""

hours = time_24_hour_format[0:2]
minutes = time_24_hour_format[3:]

if hours.isdigit() and len(hours) == 2 and minutes.isdigit() and len(minutes) == 2:
    if 0 < int(hours) < 12:
        pm_am = "am"
        hours = hours[1:]
    elif 12 < int(hours) < 24:
        pm_am = "pm"
        hours = str(int(hours) - 12)
    elif int(hours) == 12:
        pm_am = 'pm'
    elif int(hours) == 0:
        pm_am = 'am'
        hours = hours[1:]
        
else:
    print("Incorrect format")
    exit(1)

print(f"Time in 12-hour format is: {hours}:{minutes}:{pm_am}")
