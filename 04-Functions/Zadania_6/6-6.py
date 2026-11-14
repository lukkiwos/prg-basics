def f(card_number):
    return f"{card_number[:2]}{'*' * 10}{card_number[-4:]}"


if __name__ == "__main__":
    print(f("5290312400019022"))