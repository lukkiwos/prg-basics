
def issue_change_greedy(amount):
    denominations = [5, 2, 1]
    coins_count = {5: 0, 2: 0, 1: 0}
    remaining_amount = amount
    total_coins = 0

    for coin_value in denominations:
        count = remaining_amount // coin_value
        if count > 0:
            coins_count[coin_value] = count
            remaining_amount = remaining_amount % coin_value
            total_coins += count

        if remaining_amount == 0:
            break
    return coins_count, total_coins


input_amount = input("Enter the amount in PLN: ")
amount = int(input_amount)

if amount < 0:
        print("Please enter a non-negative amount (natural number).")
else:
    # Użycie funkcji i uzyskanie wyników
    result_coins, total_coins = issue_change_greedy(amount)
        
    print(f"\nThe amount of PLN {amount} in coins is:")

    for coin_value in [5, 2, 1]:
        count = result_coins[coin_value]
        if count > 0:
            print(f"{coin_value} PLN coins: {count}")
                
    print(f"\nTotal coins used: {total_coins}")