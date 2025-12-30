number_of_products = int(input("Number of products purchased: "))
product_price = int(input("Product price: "))

amount_to_pay = 0

if number_of_products <= 2:
    amount_to_pay = number_of_products * product_price

if number_of_products > 2:
    number_of_products -= 2
    amount_to_pay = (2 * product_price) + product_price * 0.75 * number_of_products

print(f"Amount to pay: {amount_to_pay:.2f}")
print()





def f(number, price):
    
    print(f"Number of products purchased: {number}")
    print(f"Product price: {price}")
    
    amount = 0
    
    if number <= 2:
        amount = number * price
    
    if number > 2:
        number -= 2
        amount = (2 * price) + product_price * 0.75 * number

    return f"Amount to pay: {amount:.2f}"


if __name__ == "__main__":
    print(f(5, 40))