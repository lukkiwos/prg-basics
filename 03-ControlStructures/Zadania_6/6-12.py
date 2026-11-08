number_of_products = int(input("Number of products purchased: "))

product_price = int(input("Product price: "))

if number_of_products < 3 and number_of_products > 0:
    amount_to_pay = number_of_products * product_price
else:
    amount_to_pay = product_price + product_price + ((number_of_products - 2) * product_price * 0.75)

print(f"Amount to pay: {amount_to_pay:.2f}")
print()


def f(number, price):
    to_pay = 0

    if number > 0 and number < 3:
        to_pay = number + price
    else:
        to_pay = price + price + ((number - 2) * price * 0.75)
    return to_pay


if __name__ == "__main__":
    print(f(5,40))