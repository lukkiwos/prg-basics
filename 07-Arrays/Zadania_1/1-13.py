# Prices of 10 products in the computer store (in currency units)
product_prices = [2999.99, 149.99, 499.99, 89.99, 1199.99, 349.99, 189.99, 99.99, 249.99, 999.99]

# Number of units available for each product
product_quantities = [5, 20, 10, 15, 7, 12, 25, 18, 9, 4]


suma = 0
count = 0

while count < len(product_prices):
    x = product_prices[count] * product_quantities[count]
    suma += x
    count += 1

print(f"Sum of all products is: {suma:.2f}")