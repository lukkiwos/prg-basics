def f(amount_to_pay):
    if amount_to_pay < 0:
        return "Kwota nie moze być ujemna"
    denominations = [5, 2, 1]
    remaining_amount = amount_to_pay
    total_coins = 0

    for coin_value in denominations:
        count = remaining_amount // coin_value
        if count > 0:
            total_coins += count
            remaining_amount %= coin_value
        if remaining_amount == 0:
            break
    return total_coins


if __name__ == "__main__":
    print(f"f(23) returns {f(23)}")
    print(f"f(8) returns {f(8)}")
    print(f"f(2) returns {f(2)}")
    print(f"f(0) returns {f(0)}")