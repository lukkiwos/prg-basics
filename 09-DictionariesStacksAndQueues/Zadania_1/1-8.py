import math

price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

print("List of products and their prices before the discount: ")
for name, price in price_list.items():
    print(f"{name}: {price}")

print()
total_price = sum(price_list.values())
print(total_price)

print()
for name, price in price_list.items():
    new_price = price * 0.9
    rounded_price = round(new_price, 2)
    price_list[name] = rounded_price
    print(f"{name}: {rounded_price}")

print()
total_discount = sum(price_list.values())
print(total_discount)