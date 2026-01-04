def f(palindrome):
    reverse = palindrome[::-1]

    if palindrome == reverse:
        return True
    else:
        return False




if __name__ == "__main__":
    print(f("radar"))       # returns True
    print(f("12-11-21"))    # returns True
    print(f("book"))        # returns False