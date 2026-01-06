def f(palindrom):

    reverse = "".join(reversed(palindrom))

    if palindrom == reverse:
        return True

    return False




if __name__ == "__main__":
    print(f("radar"))
    print(f("12-11-21"))
    print(f("book"))



# NIE udało mi się zrobić samemu