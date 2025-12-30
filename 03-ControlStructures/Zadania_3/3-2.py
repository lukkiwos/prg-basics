###
# Checking login and password
#
login = 'joe'
password = 'abcd'

entered_login = input('Login: ')
entered_password = input('Password: ')

if login == entered_login and password == entered_password:
    print('You are logged in')
else:
    print('Incorrect login or password!!')

print()


def f(entered_login, entered_password):
    login = "HWDP"
    password = "2137"
    
    if login == entered_login and password == entered_password:
        return "Jesteś zalogowany"
    else:
        return "Niepoprawny login lub hasło"
    

if __name__ == "__main__":
    print(f("HWDP", "2137"))