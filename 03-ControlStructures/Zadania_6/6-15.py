# EAN-13 (European Article Number) is a barcode for marking goods. 
# The first 3 digits (590) usually indicate goods manufactured in Poland. 
# Write a program that checks whether the EAN-13 number 
# entered from the keyboard consists of exactly 13 characters (digits).
# Print a message if the number is correct. 
# Additionally, only when the article number is correct, 
# print a message when the product was manufactured in Poland.

ean_code = input("Enter EAN-13 article number: ")

len_code = len(ean_code)

if len_code == 13:
    print("Article number is CORRECT")
    
    if ean_code[0:3] == "590":
        print("Article manufactured in POLAND")

else:
    print("Article number is INCORRECT")

