bottles = [508, 500, 512, 499, 492, 511, 503, 476, 501, 509]

capacity = 500
tolerance = 0.02  # 2%

def incorrect_fill(capacity, tolerance):
    min_fill = capacity * (1 - tolerance)
    max_fill = capacity * (1 + tolerance)
    return lambda value: value < min_fill or value > max_fill

incorrect = list(filter(incorrect_fill(capacity, tolerance), bottles))

percentage = len(incorrect) / len(bottles) * 100

print(f"Bottle capacity:    {capacity}ml")
print(f"Filling tolerance:  {int(tolerance*100)}%")
print("Filled bottles:     " + ",".join(map(str, bottles)))
print(f"Incorrectly filled: {int(percentage)}%")
