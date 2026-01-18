speed = [48, 47, 54, 50, 42, 68, 39, 46]
max_speed = 50

too_high = list(filter(lambda value: value > max_speed, speed))


print(f"Recorded values: {", ".join(map(str, speed))}")

print(f"Speed too high: {", ".join(map(str, too_high))}")