def f(binary_number):

    for x in binary_number:
        if x != "1" and x != "0":
            return False
        
    return True



if __name__ == "__main__":
    print(f("101101"))
    print(f("1311a10100"))



# UDAŁO mi się zrobić samemu