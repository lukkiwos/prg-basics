import converters

print('### Test converters')
print(f'Three meters is: {converters.m_to_cm(3)}cm')
print(f"Twenty centimeters is: {converters.cm_to_m(20)}m")
print(f"Thirty centimeters is: {converters.cm_to_inch(30)} inches")
print(f"5'11 is: {converters.feet_inch_to_cm(5,11)}cm")
