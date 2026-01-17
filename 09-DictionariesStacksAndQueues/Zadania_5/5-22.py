import json

product = {}

# read product data from keyboard
product["name"] = input("Enter product name: ")

# read price as float
while True:
    try:
        price_input = input("Enter product price (e.g., 12.99): ")
        product["price"] = float(price_input)
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# read paid status as boolean
while True:
    paid_input = input("Has the product been paid? (yes/no): ").strip().lower()
    if paid_input == "yes":
        product["paid"] = True
        break
    elif paid_input == "no":
        product["paid"] = False
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

# save product data to json file
with open("product.json", "w", encoding="utf-8") as file:
    json.dump(product, file, indent=4)

print("Product data saved to product.json")
