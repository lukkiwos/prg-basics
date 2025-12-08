
print("SURVEY")
computer_science = input("Are you interested in computer science? (y/n): ")
computer_games = input("Do you like playing computer games? (y/n): ")
instagram = input("Do you like an Instagram account? (y/n): ")

print()
print("SURVEY RESULTS")

computer_science_answer = "Interested in computer science:"
computer_games_answer = "Playing computer games:"
instagram_answer = "Has an Instagram account:"


if computer_science == 'y':
    print(f"{computer_science_answer} Yes")
else:
    print(f"{computer_science_answer} No")

if computer_games == 'y':
    print(f"{computer_games_answer} Yes")
else:
    print(f"{computer_games_answer} No")

if instagram == 'y':
    print(f"{instagram_answer} Yes")
else:
    print(f"{instagram_answer} No")