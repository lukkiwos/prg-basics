def avg_speed(distance, hours, minutes):
    full_time = hours + (minutes / 60)

    avg = distance / full_time
    
    return avg


distance1 = int(input("Enter distance in km: "))
hours1 = int(input("Enter number of travel hours: "))
minutes1 = int(input("Enter number of travel minutes: "))

print(f"Average speed: {avg_speed(distance1, hours1, minutes1):.1f} km/h")