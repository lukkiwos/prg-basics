def f(size1,size2):

    if size1 == "S":
        weight_1 = 1
    elif size1 == "M":
        weight_1 = 2
    else:
        weight_1 = 3

    if size2 == "S":
        weight_2 = 1
    elif size2 == "M":
        weight_2 = 2
    else:
        weight_2 = 3



    if weight_1 > weight_2:
        return 1
    elif weight_1 < weight_2:
        return 2
    else:
        return 0




if __name__ == "__main__":
    print(f("L", "S"))
    print(f("M", "L"))



# NIE udało mi się zrobić