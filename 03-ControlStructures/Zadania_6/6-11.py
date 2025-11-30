current_price = 140
previous_price = 200

print(f"Current product price: {current_price}")
print(f"Previous product price: {previous_price}")

decreased_price = ((previous_price - current_price) / previous_price) * 100

if decreased_price >= 0.1:
    print(f"Buy the product!!\n Product price reduced by {decreased_price:.0f}%")
