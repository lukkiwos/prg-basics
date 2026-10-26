###
# Checking login and password
#
login = 'joe'
password = 'abcd'
entered_login = input('Login: ')
entered_password = input('Password: ')
if login == entered_login and password == entered_password :
    print('You are logged in')
else:
    print('Incorrect login or password!!')
print()


def f(log, passw):
    login1 = "joel"
    password1 = "1234"

    if log == login1 and passw == password1:
        return "You are logged in"
    else:
        return "Incorrect password or login"


if __name__ == "__main__":
    print(f("joel", "1234"))
    print(f("joooo", "9876"))