computer_science = input("SURVEY Are you interested in computer science? (y/n): ")
computer_games = input("Do you like playing computer games? (y/n): ")
instagram = input("Do you have an Instagram account? (y/n): ")
print()

if computer_science == "y":
    computer_science = True
else:
    computer_science = False

if computer_science == True:
    display_science = "Yes"
else:
    display_science = "No"


if computer_games == "y":
    computer_games = True
else:
    computer_games = False

if computer_games == True:
    display_games = "Yes"
else:
    display_games = "No"


if instagram == "y":
    instagram = True
else:
    instagram = False

if instagram == True:
    display_instagram = "Yes"
else:
    display_instagram = "No"


print(f"SURVEY RESULTS Interested in computer science: {display_science}")
print(f"Playing computer games: {display_games}")
print(f"Has an Instagram account: {display_instagram}")
