
pin_code = '0805'

count = 0
max_attempts = 3

while max_attempts > count:
    pin = input("Enter the PIN code: ")
    
    if pin == pin_code:
        print("Access granted")
        break
    
    else:
        print("Incorrect...")
    
    count += 1

if count == max_attempts:
    print("Sorry, your payment card has been blocked.")

print()
print()
print()
print()




def f():
    pin_code = '0805'
    count = 0
    max_attemps = 3

    while count < max_attempts:
        pin = input("Enter the PIN code: ")

        if pin == pin_code:
            print("Success granted")
            break
        else:
            print("Incorrect...")
        count += 1

    if count == max_attemps:
        print("Sorry, your payment card has been blocked.")


if __name__ == "__main__":
    print(f())