###
# Calculates the total value of money spent
#
import re # module for regular expressions

# file name with shopping report
email_file = 'report.txt'

# read the content of email
with open(email_file, 'r', encoding="utf-8") as email:
    email_content = email.read()

# regular expression pattern
# for amounts
pattern = r'€\d+'

# extract numbers from email
# tip: findall() method returns an array
amounts = re.findall(pattern, email_content)

# calculate the total purchases
suma = 0
for amount in amounts:
    num = amount.replace('€','')
    suma += int(num)

# print result
print(f"Total value of money spent is: €{suma}")