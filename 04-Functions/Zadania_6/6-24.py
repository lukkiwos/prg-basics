def f(expression):
    result = 0
    current_operator = "+"
    
    for x in expression:
        if x != "+" and x != "-":
            x = int(x)
            if current_operator == "+":
                result += x
            elif current_operator == "-":
                result -= x

        if x == "+" or x == "-":
            current_operator = x

    return result




if __name__ == "__main__":
    print(f("2+3"))            # returns 5
    print(f("3+8+1"))          # returns 12
    print(f("2+3-4+5-0"))      # returns 6