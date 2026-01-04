def hide(card_number):
    
    number = len(card_number) - len(card_number[0:2]) - len(card_number[-4])
    hided = number * "*"
    result = card_number[0:2] + hided + card_number[12:]

    return result


if __name__ == "__main__":
    print(hide("5290312400019022"))