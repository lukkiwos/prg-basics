def f(dice):
    current_count = 1
    max_count = 1
    previous_digit = None
    max_digit = None
    
    for x in dice:
        if x == previous_digit:
            current_count += 1
        else:
            current_count = 1


        if current_count > max_count:
            max_count = current_count
            max_digit = x
        
        previous_digit = x
    
    return max_digit





if __name__ == "__main__":
    print(f("5233165554211"))        # returns 5
    print(f("2133"))                 # returns 3