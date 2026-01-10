computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]
count = 0
number = 1
x = sorted(computer_games)

while count < len(computer_games):
    print(number, x[count])
    count += 1
    number += 1