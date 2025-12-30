print("SURVEY")
x = input("Are you interested in computer science? (y/n): ")
y = input("Do you like playing computer games? (y/n): ")
z = input("Do you have an instagram account? (y/n): ")
print()

interested_cs = x == "y"
playing_cg = y == "y"
instagram_acc = z == "y"


print("SURVEY RESULTS")

if interested_cs:
    print(f"Interested in computer science: Yes")
else:
    print(f"Interested in computer science: No")

if playing_cg:
    print("Playing computer games: Yes")
else:
    print("Playing computer games: No")

if instagram_acc:
    print("Has an Instagram account: Yes")
else:
    print("Has an Instagram account: No")
print()





def f(cs, cg, ig):
    x = cs == "y"
    y = cg == "y"
    z = ig == "y"

    if x:
        print("Interested in computer science: Yes")
    else:
         print("Interested in computer science: No")
    
    if y:
        print("Playing computer games: Yes")
    else:
        print("Playing computer games: No")

    if z:
        print("Has an Instagram account: Yes")
    else:
        print("Has an Instagram account: No")
    return "SURVEY RESULTS"


if __name__ == "__main__":
    print(f("y","n","y"))