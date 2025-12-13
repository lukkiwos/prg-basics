def hide(card_number):
    if len(card_number) != 16 or not card_number.isdigit():
        return "Invalid Card Number Format"
    first_two = card_number[0:2]
    last_four = card_number[-4:]
    mask = "*" * 10

    masked_cart = f"{first_two}{mask}{last_four}"
    return masked_cart

if __name__ =="__main__":
    sample_card = "5290312400019022"
    result = hide(sample_card)
    print(f"Sample card is: {sample_card}\n Result is: {result}")