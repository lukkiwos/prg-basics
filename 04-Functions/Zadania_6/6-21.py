def f(number1, number2, number3):
    
    lista = [number1, number2, number3]

    biggest_number = max(lista)
    smallest_number = min(lista)

    difference = biggest_number - smallest_number

    return difference




if __name__ == "__main__":
    print(f(7,4,9))     # returns 5
    print(f(2,12,8))    # returns 10