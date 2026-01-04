import converters

print('### Test converters')
print()
print(f'Three meters is:                {converters.m_to_cm(3):.2f}cm')                     # 1
print(f'Three houndred centimeters is:  {converters.cm_to_m(300):.2f}m')                    # 2
print(f"Twenty centimeters is:          {converters.cm_to_inch(20):.2f} inches")
print(f"Three houndred feets is:        {converters.feet_to_cm(300):.2f} feets")
print(f"Ten inches is:                  {converters.inch_to_cm(10):.2f}cm")
