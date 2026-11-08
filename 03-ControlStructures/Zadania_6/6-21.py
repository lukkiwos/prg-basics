amount = int(input("Enter the amount in PLN: "))
amount1 = amount
count_5 = 0
count_2 = 0
count_1 = 0

while amount != 0:
    count_5 = amount // 5
    amount = amount % 5

    count_2 = amount // 2
    amount = amount % 2

    count_1 = amount // 1
    amount = amount % 1


print(f"The amount of PLN {amount1} in coins: ")
print(f"5 PLN coins: {count_5}")
print(f"2 PLN coins: {count_2}")
print(f"1 PLN coins: {count_1}")
print()


def f(ilosc):
    ilosc1 = ilosc
    piec = 0
    dwa = 0
    jeden = 0

    while ilosc != 0:
        piec = ilosc // 5
        ilosc = ilosc % 5

        dwa = ilosc // 2
        ilosc = ilosc % 2

        jeden = ilosc // 1
        ilosc = ilosc % 1

    return f"Kwota {ilosc1} PLN w monetach: \nMonety 5 PLN: {piec} \nMonety 2 PLN: {dwa} \nMonety 1 PLN: {jeden} \n"


if __name__ == "__main__":
    print(f(12))
    print(f(60))
    print(f(89))
    print(f(91))