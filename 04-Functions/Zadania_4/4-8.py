def time_string(hours, minutes, time_format):
    if time_format == '24':
        return f"{hours:02d}:{minutes:02d}"

    elif time_format == '12':
        suffix = "AM" if hours < 12 else "PM"
        if hours == 0:
            display_hours = 12
        elif hours > 12:
            display_hours = hours - 12
        else:
            display_hours = hours
        return f"{display_hours}:{minutes:02d}{suffix}"
    
print(f"{time_string(15, 38, '24')}")
print(f"{time_string(8, 3, '24')}")
print(f"{time_string(0, 5, '24')}")

print(f"{time_string(11, 15, '12')}")
print(f"{time_string(0, 7, '12')}")
print(f"{time_string(7, 30, '12')}")
print(f"{time_string(12, 46, '12')}")
print(f"{time_string(13, 10, '12')}")
print(f"{time_string(19, 2, '12')}")