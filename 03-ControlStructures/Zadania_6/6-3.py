###
# House lighting with three bulbs and two switches
# Checking how many bulbs are illuminating the house
#
light_switch1 = False # False - switch off, True - switch on
light_switch2 = True
bulbs_on = 0
if light_switch1:
    bulbs_on += 1
if light_switch2:
    bulbs_on += 2

print(f"There are {bulbs_on} bulbs on")
print()


def f(first, second):
    bulbs = 0
    if first == "Y":
        bulbs += 1
    if second == "Y":
        bulbs += 2

    return bulbs


if __name__ == "__main__":
    print(f("Y","N"))