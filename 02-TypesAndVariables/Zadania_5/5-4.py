#23% VAT was paid from an amount. Write a program that reads an amount from the keyboard. 
# Then, it calculates and prints both the amount and its VAT. 
# Apply formatting with two decimal places. Sample result:

#Amount  : 15.84
#VAT 23% :  3.64

amount = input("Enter the amount including VAT: ")
amount = float(amount)

vat = amount * 0.23

print(f"Amount  : {amount:.2f}")
print(f"Vat 23% : {vat:.2f}")