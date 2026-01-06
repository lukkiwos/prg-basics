def f(card_number):

    number = len(card_number) - len(card_number[0:2]) - len(card_number[12:])
    hided = number * "*"

    result = card_number[0:2] + hided + card_number[12:]

    return result




if __name__ == "__main__":
    print(f("5290312400019022"))




# NIE udało mi się zrobić samemu