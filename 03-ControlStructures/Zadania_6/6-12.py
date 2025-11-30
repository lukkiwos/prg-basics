# In one of the online stores, a 25% discount is charged 
# for each product purchased over two. 
# Write a program that calculates the amount to be paid. 
# Read the number of purchased products 
# and the product price from the keyboard.


number_of_products = int(input("Number of products purchased: "))
product_price = float(input("Product price: "))

discount = 0.75

if number_of_products % 2 == 0:
    amount_to_pay = number_of_products * product_price * discount
    num_discounted = number_of_products
    num_full_price = 0

else:
    num_discounted = number_of_products - 1
    num_full_price = 1
    cost_discounted = num_discounted * product_price * discount
    cost_full_price = num_full_price * product_price

    amount_to_pay = cost_discounted + cost_full_price

print(f'Amount to pay: {amount_to_pay:.2f}')