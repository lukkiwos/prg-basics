def f(binary_number):
    
    for x in binary_number:
        if not x == '0' and not x == '1':
            return False
    
    return True






if __name__ == "__main__":
    print(f("101101"))
    print(f("1311a10100"))