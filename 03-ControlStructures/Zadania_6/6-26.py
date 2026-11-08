pin = "0805"

for x in range(1,4):
    code = input("Enter the PIN code: ")
    if code == pin:
        print("You are logged in")
        break
    else:
        print("Incorrect...")

if code != pin:
    print("Sorry, your payment card has been blocked.")