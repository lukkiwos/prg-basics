def f(dice):
    current_number = dice[0]
    passa = 1

    best_number = dice[0]
    rekord = 1

    for x in dice[1:]:
        if x == current_number:
            passa += 1
        else:
            current_number = x
            passa = 1
        if passa > rekord:
            rekord = passa
            best_number = current_number

    return int(best_number)


if __name__ == "__main__":
    print(f("5233165554211"))
    print(f("2133"))