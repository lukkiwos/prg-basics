###
# Calculates and prints the total washing time.
#
# A washing machine allows you to wash a jacket, which takes
# 40 minutes, wash underwear, which takes 70 minutes, and wash shoes,
# which takes 20 minutes. In addition, it is possible to program
# an additional rinse (15 minutes) and an additional spin (9 minutes).
#

jacket = 40
underwear = 70
shoes = 20

extra_rinse = 15
extra_spin = 9

total_washing_time = 0


program = input('Select washing program (jacket, underwear, shoes): ').lower()
extra_rinse = input('Extra rinse? (y/n) ').lower() == 'y'
extra_spin = input('Extra spin? (y/n) ').lower() == 'y'


if program == 'jacket':
    total_washing_time += jacket

elif program == 'underwear':
    total_washing_time += underwear

elif program == 'shoes':
    total_washing_time += shoes

else:
    print("Invalid washing program selected")


if extra_rinse:
    total_washing_time += extra_rinse

if extra_spin:
    total_washing_time += extra_spin


print(f"\nTotal washing time: {total_washing_time} minutes.")