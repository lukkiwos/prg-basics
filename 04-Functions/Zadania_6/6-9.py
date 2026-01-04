def f(number, even):

    number = str(number)
    sum_even = 0
    sum_odd = 0

    if even:
        for x in number:
            digit = int(x)
            if digit % 2 == 0:
                sum_even += digit
        return sum_even
    
    else:
        for y in number:
            digit_2 = int(y)
            if not digit_2 % 2 == 0:
                sum_odd += digit_2
        return sum_odd

    





if __name__ == "__main__":
    print(f(3124,True))        # returns 6
    print(f(3124,False))       # returns 4
    print(f(20576,False))      # returns 12
    print(f(20576,True))       # returns 8
    print(f(13115,True))       # returns 0