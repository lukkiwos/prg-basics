def f(number):

    a = 0
    b = 1

    while b < number:
        c = a + b
        a = b
        b = c

    if b == number:
        return True
    else: 
        return False






if __name__ == "__main__":
    print(f(5))
    print(f(7))



# NIE udało mi się zrobić