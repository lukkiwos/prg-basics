def f(password):
    if len(password) >= 6:
        for x in password:
            character = password.count(x)
            if character > 1:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    print(f("ax15"))
    print(f("book123"))
    print(f("A2water3"))
    print(f("qwerty"))
    print(f(""))