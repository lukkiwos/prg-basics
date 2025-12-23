###
# A program that prints a numerical representation of each letter of your name.
#

name = 'Łukasz' # replace John with your name

print(f'The letter {name[0]} has a code: {ord(name[0])}')
print(f'The letter {name[1]} has a code: {ord(name[1])}')
print(f"The letter {name[2]} has a code: {ord(name[2])}")
print(f"The letter {name[3]} has a code: {ord(name[3])}")
print(f"The letter {name[4]} has a code: {ord(name[4])}")
print(f"The letter {name[5]} has a code: {ord(name[5])}")
print()


def f(name):
    name2 = []
    #name3 = []
    for x in name:
        #print(f"x = {x}, x[0:] = {x[0:]}")
        name2.append(str(ord(x)))
        
    #for y in name2:
        #name3.append(str(y))
    return " ".join(name2)

if __name__ == "__main__":
    result = f("Łukasz")
    print(result)