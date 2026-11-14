def f(amount_to_pay):
    coins = 0

    coins = coins + amount_to_pay // 5
    amount_to_pay = amount_to_pay % 5

    coins = coins + amount_to_pay // 2
    amount_to_pay = amount_to_pay % 2

    coins = coins + amount_to_pay // 1

    return coins


if __name__ == "__main__":
    print(f(23))
    print(f(8))
    print(f(2))
    print(f(0))