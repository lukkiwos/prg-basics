def f(amount_to_pay):
    
    coins_5 = amount_to_pay // 5
    remain_5 = amount_to_pay % 5

    coins_2 = remain_5 // 2
    remain_2 = remain_5 % 2

    coins_1 = remain_2 // 1


    result = coins_5 + coins_2 + coins_1

    return result




if __name__ == "__main__":
    print(f(23))
    print(f(8))



# UDAŁO mi się zrobić samemu