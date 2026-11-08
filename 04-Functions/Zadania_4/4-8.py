def time_string(hours, minutes, time_format):
    
    if time_format == "24":
        if hours < 10:
            if minutes < 10:
                return f"0{hours}:0{minutes}"
            elif minutes >= 10:
                return f"0{hours}:{minutes}"
        
        elif hours >= 10:
            if minutes < 10:
                return f"{hours}:0{minutes}"
            elif minutes >= 10:
                return f"{hours}:{minutes}"
    
    elif time_format == "12":
        if hours == 0:
            if minutes < 10:
                return f"12:0{minutes}am"
            elif minutes > 10:
                return f"12:{minutes}am"
        
        elif hours > 0 and hours < 12:
            if minutes < 10:
                return f"{hours}:0{minutes}am"
            elif minutes >= 10:
                return f"{hours}:{minutes}am"
                
        elif hours == 12:
            if minutes < 10:
                return f"{hours}:0{minutes}pm"
            elif minutes >= 10:
                return f"{hours}:{minutes}pm"
            
        elif hours > 12 and hours < 24:
            if minutes < 10:
                return f"{hours - 12}:0{minutes}pm"
            if minutes >= 10:
                return f"{hours - 12}:{minutes}pm"


if __name__ == "__main__":
    print(time_string(15,38,"24"))      # returns '15:38'
    print(time_string(8, 3, "24"))      # returns '08:03'
    print(time_string(0, 5, "24"))      # returns '00:05'
    print(time_string(11, 15, '12'))    # returns '11:15am'
    print(time_string(0, 7, '12'))      # returns '12:07am'
    print(time_string(7, 30, '12'))     # returns '7:30am'
    print(time_string(12, 46, '12'))    # returns '12:46pm'
    print(time_string(13, 10, '12'))    # returns '1:10pm'
    print(time_string(19, 2, '12'))     # returns '7:02pm'
