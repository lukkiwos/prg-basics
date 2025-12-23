###
# A program that calculates and prints
# the average grade of a student
#
math = 5
art = 4
music = 5
history = 3
average = (math + art + music + history) / 4
print("Average grade is", average)
print()



def f(math, ang, inf, fiz):
    srednia = (math + ang + inf + fiz) / 4
    return srednia

if __name__ == "__main__":
    print(f"Średnia podanych ocen to: {f(3, 1, 5, 6):.2f}")