def time_string(hours, minutes, time_format):
    
    if time_format == "24":
        if hours >= 10 and hours <= 23: 
            if minutes >= 10 and minutes <= 59:
                return f"{hours}:{minutes}"
            elif minutes >= 0 and minutes <= 9:
                return f"{hours}:0{minutes}"
        
        elif hours >= 0 and hours <= 9:
            if minutes >= 10 and minutes <= 59:
                return f"0{hours}:{minutes}"
            elif minutes >= 0 and minutes <= 9:
                return f""
        else:
            return "Incorrect number of hours or minutes"
        
    elif time_format == "12":
        if hours >= 1 and hours <= 11 and minutes >= 0 and minutes <= 59:
            return f"{hours}:{minutes}am"
        elif hours == 0 and minutes >= 0 and minutes <= 59:
            return f"12:{minutes}am"
        