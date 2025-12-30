current_price = 140.00
previous_price = 200.00

print(f"Current product price: {current_price}")
print(f"Previous product price: {previous_price}")


x = current_price / previous_price 
y = (1 - x) * 100

if y >= 0.1:
    print("Buy the product!!!")
    print(f"Product price reduced by {y:.0f}%")

print()






def f(current_price, previous_price):
    x = current_price / previous_price
    y = (1 - x) * 100
    return f"Buy the product! Product price reduced by {y:.0f}%"


if __name__ == "__main__":
    print(f(140, 200))