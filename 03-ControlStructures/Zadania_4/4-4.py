###
# Prints the name of university where you are studying
# with an extra space between characters (add a space between
# each character), e.g.
# 'book' -> 'b o o k'
#
university = 'Krakow University of Economics'
university_expanded = ''

for char in university:
    university_expanded = university_expanded + char + " "

print(university) # original university name
print()
print(university_expanded) # expanded university name
print()



def f(text):
    text_expanded = ""
    for char in text:
        text_expanded = text_expanded + char + " "
    return text_expanded


if __name__ == "__main__":
    print(f("Jebać policję"))