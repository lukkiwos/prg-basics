###
# House lighting with three bulbs and two switches
# Checking how many bulbs are illuminating the house
#
light_switch1 = True # False - switch off, True - switch on
light_switch2 = False

bulbs_on = 0

if light_switch1:
    bulbs_on += 1
if light_switch2:
    bulbs_on += 2
print(f"There are {bulbs_on} bulbs on right now.")
print()




def f(switch_1, switch_2):
    bulbs_on = 0

    if switch_1:
        bulbs_on += 1
    if switch_2:
        bulbs_on += 2
    return f"W tym momencie świecą/ci się {bulbs_on} zarówki/a"


if __name__ == "__main__":
    print(f(True, True))