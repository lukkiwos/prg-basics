###
# Password validator
# New password is at least 12 characters long
#
new_password = input('Enter new password: ')

if len(new_password) < 12:
   print('Password too short (min. 12 chars)') 

print()




def f(password):
    if len(password) < 10:
        print("Password too short")
    
    return f"Your new password is: {password}"



if __name__ == "__main__":
    print(f("1234567891"))