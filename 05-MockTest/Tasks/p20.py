def f(time1, time2):
    def to_minutes(time_str):
        time_str = time_str.strip()


        if "AM" in time_str or "PM" in time_str:
            parts = time_str.split()
            hour, minute = parts[0].split(":")
            hour = int(hour)
            minute = int(minute)
            period = parts[1]

            if period == "AM":
                if hour == 12:
                    hour = 0
            else:
                if hour != 12:
                    hour += 12
        else:
            hour, minute = time_str.split(":")
            hour = int(hour)
            minute = int(minute)

        return hour * 60 + minute

    t1 = to_minutes(time1)
    t2 = to_minutes(time2)

    if t1 <= t2:
        return time1
    else:
        return time2
    





if __name__ == "__main__":
    print(f("08:30", "12:45"))
    print(f("2:30 PM", "11:15 AM"))


# NIE udało mi się zrobić