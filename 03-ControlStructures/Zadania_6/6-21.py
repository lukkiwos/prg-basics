amount = int(input("Enter the amount in PLN: "))
real_amount = amount


print(f"The amount of PLN {real_amount} in coins: ")


# Coins of 5 PLN
coins_5 = amount // 5
remaining_amount = amount % 5
print(f"5 PLN coins: {coins_5}")


# Coins of 2 PLN
coins_2 = remaining_amount // 2
remaining_amount = remaining_amount % 2
print(f"2 PLN coins: {coins_2}")


# Coins of 1 PLN
coins_1 = remaining_amount
print(f"1 PLN coins: {coins_1}")

print()
print()





def f(amount):
    real_amount = amount


    coins_5 = amount // 5
    remaining_amount = amount % 5
    print(f"5 PLN w monetach: {coins_5}")


    coins_2 = remaining_amount // 2
    remaining_amount = remaining_amount % 2
    print(f"2 PLN w monetach: {coins_2}")


    coins_1 = remaining_amount
    print(f"1 PLN w monetach: {coins_1}")
    
    return f"Wprowadzona kwota to: {real_amount} PLN"


if __name__ == "__main__":
    print(f(18))