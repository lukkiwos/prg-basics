def time_string(hours, minutes, time_format):
    am_or_pm = ""


    if time_format == '24':
        hours = hours
        minutes = minutes
        
        return f"{hours:02}:{minutes:02}"

    
    elif time_format == '12':
        if hours == 0:
            hours = 12
            am_or_pm = "am"
        elif hours < 12:
            am_or_pm = "am"
        elif hours > 12:
            hours -= 12
            am_or_pm = "pm"
        elif hours == 12:
            am_or_pm = "pm"

        return f"{hours}:{minutes:02}{am_or_pm}"



if __name__ == "__main__":
    print(time_string(15, 38, '24'))           # returns '15:38'
    print(time_string(8, 3, '24'))             # returns '08:03'
    print(time_string(0, 5, '24'))             # returns '00:05'
    print(time_string(11, 15, '12'))           # returns '11:15am'
    print(time_string(0, 7, '12'))             # returns '12:07am'
    print(time_string(7, 30, '12'))            # returns '7:30am'
    print(time_string(12, 46, '12'))           # returns '12:46pm'
    print(time_string(13, 10, '12'))           # returns '1:10pm'
    print(time_string(19, 2, '12'))            # returns '7:02pm'