ean = input("Enter EAN-13 article number: ")

if len(ean) == 13:
    print("Article number is correct")
    if ean[0:3] == "590":
        print("Article manufactured in Poland")

print()


def f(ean13):
    if len(ean13) == 13:
        if ean13[0:3] == "590":
            return "Correct, Poland"
        else:
            return "Correct"
    


if __name__ == "__main__":
    print(f("5901230094938"))
    print(f("5911230094938"))