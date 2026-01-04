def f(password):

    if len(password) < 6:
        return False
    
    for x in password:
        if password.count(x) > 1:
            return False
            
    return True





if __name__ == "__main__":
    print(f("ax15"))            # returns False
    print(f("book123"))         # returns False
    print(f("A2water3"))        # returns True
    print(f("qwerty"))          # returns True
    print(f(""))                # returns False