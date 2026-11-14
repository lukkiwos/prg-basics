def f(palindrome):
    palindrome1 = ""

    for x in palindrome:
        palindrome1 = x + palindrome1

    if palindrome == palindrome1:
        return True
    else:
        return False


if __name__ == "__main__":
    print(f("radar"))
    print(f("12-11-21"))
    print(f("book"))