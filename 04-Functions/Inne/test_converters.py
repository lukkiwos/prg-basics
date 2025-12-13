import converters

print('### Test converters')
print()
print(f'Three meters is:                {converters.m_to_cm(3):.2f}cm')                     # 1
print(f'Three houndred centimeters is:  {converters.cm_to_m(300):.2f}m')                    # 2
print(f'Ten cenimeters is:              {converters.cm_to_inch(10):.2f} inches')            # 3
print(f'Five inches is:                 {converters.inch_to_cm(5):.2f}cm')                  # 4
print(f'Three feets is:                 {converters.feet_to_inch(3):.2f} inches')           # 5
