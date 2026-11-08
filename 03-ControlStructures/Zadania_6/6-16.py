###
# Calculates and prints the total washing time.
#
# A washing machine allows you to wash a jacket, which takes
# 40 minutes, wash underwear, which takes 70 minutes, and wash shoes,
# which takes 20 minutes. In addition, it is possible to program
# an additional rinse (15 minutes) and an additional spin (9 minutes).
#
total_washing_time = 0
program = input('Select washing program: (J)acket, (U)nderwear, (S)hoes: ')
extra_rinse = input('Extra rinse? (Y/N): ')
extra_spin = input('Extra spin? (Y/N): ')

if program == "J":
    total_washing_time += 40
elif program == "U":
    total_washing_time += 70
elif program == "S":
    total_washing_time += 20
if extra_rinse == "Y":
    total_washing_time += 15
if extra_spin == "Y":
    total_washing_time += 9

print(f"Total washing time: {total_washing_time} minutes")
print()


def f(p,r,s):
    time = 0

    if p == "j":
        time += 40
    elif p == "u":
        time += 70
    elif p == "s":
        time += 20
    if r == "T":
        time += 15
    if s == "T":
        time += 9

    return time


if __name__ == "__main__":
    print(f("s", "T", "F"))