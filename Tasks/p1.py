def f(player1, player2):
    
    player1_score = calculate_player_score(player1)
    player2_score = calculate_player_score(player2)
    
    print(player1_score)
    print(player2_score)

    result = player1_score >= player2_score

    return result





def calculate_player_score(player):
    cards = {
        'A': 10,
        'K': 10,
        'Q': 10,
        'J': 10,
        'T': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2,
    }

    values = []
    
    for letter in player:
        # print(letter)
        x = cards.get(letter)
        values.append(x)
        player1_sum = sum(values)
    return player1_sum
   
    



if __name__ == "__main__":
    print(f("AJ972","AQT72"))
    print()
    print(f("9532","K8"))





   # for card, value in cards.items():
        # print(card, value)