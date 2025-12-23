speed = int(input("Enter vehicle speed: "))
speed_ok = speed >= 40 and speed <= 140
print(f"Speed is valid: {speed_ok}")
print()


def f(speed):
    ok_speed = speed >= 40 and speed <= 140
    return ok_speed

if __name__ == "__main__":
    print(f(139))