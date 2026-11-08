current_price = 140
previous_price = 200

reduced_price = (1 - (current_price / previous_price)) * 100

if reduced_price >= 0.1:
    print("Buy the product!")
    print(f"Product price reduced by {reduced_price:.0f}%")
print()



def f(current, previous):
    reduced = 1 - (current / previous)

    if reduced >= 0.1:
        return f"Buy the product!\nProduct price reduced by {reduced:.0%}"
        # return True
    # else:
        # return False


if __name__ == "__main__":
    print(f(160, 200))