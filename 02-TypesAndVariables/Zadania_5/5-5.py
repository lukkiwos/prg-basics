# The price of the product on the price tag is given before and after the discount is applied. 
# Write a program that allows you to enter the product price and discount. 
# Print the product price, discount, discounted product price, 
# and the difference between the product price before and after the discount. 
# Print all prices with two decimal places.

product_price = input("Enter price: ")
product_price = float(product_price)

discount = input("Enter discount %: ")
discount = float(discount)

after_discount = product_price - (product_price * discount / 100)
difference = product_price - after_discount

print(f"Price with discount: {after_discount:.2f}")
print(f"Reduction: {difference:.2f}")