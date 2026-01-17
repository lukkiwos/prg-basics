price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

print("Before the discount: ")
suma = 0

for key, value in price_list.items():
   print(f"{key} : {value}")
   suma += value

print()
print(f"Total value of the products before the discount: {suma:.2f}")
print()
print()



print("After discount (10%): ")
suma2 = 0

for key, value in price_list.items():
   value *= 0.9
   suma2 += value
   print(f"{key} : {value:.2f}")
   
   
print()
print(f"Total value of the products after the discount: {suma2:.2f}")
print()
