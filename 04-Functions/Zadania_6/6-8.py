def f(amount_to_pay):
    
    number_of_5 = amount_to_pay // 5
    remainder_after_5 = amount_to_pay % 5

    number_of_2 = remainder_after_5 // 2
    remainder_after_2 = remainder_after_5 % 2

    number_of_1 = remainder_after_2 // 1
    

    coins_sum = number_of_5 + number_of_2 + number_of_1

    return coins_sum









if __name__ == "__main__":
    print(f(23))
    print(f(8))
    print(f(2))
    print(f(0))