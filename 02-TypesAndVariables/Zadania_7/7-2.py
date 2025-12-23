###
# A program that checks whether the password length
# read from the keyboard is correct.
#
password = input('Enter password: ')
password_ok = len(password) >= 8

print(f'Password length is valid: {password_ok}')
print()



def f(password):
    password_ok = len(password) >= 8
    return password_ok

if __name__ == "__main__":
    print(f("university"))
    print(f("peter123"))
    print(f("seven"))
    print(f("anna333"))