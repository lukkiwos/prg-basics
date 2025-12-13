# Prices of 10 products in the computer store (in currency units)
product_prices = [2999.99, 149.99, 499.99, 89.99, 1199.99, 
349.99, 189.99, 99.99, 249.99, 999.99]

# Number of units available for each product
product_quantities = [5, 20, 10, 15, 7, 12, 25, 18, 9, 4]


total_store_value = 0

for price, quantity in zip(product_prices, product_quantities):
    asset_value = price * quantity
    total_store_value += asset_value



print()
print(f"Cena produktów: {product_prices}")
print(f"Dostępna ilość: {product_quantities}")
print()
print(f"Całkowita wartość wszystkich zasobów w sklepie: {total_store_value:.2f}")
print()