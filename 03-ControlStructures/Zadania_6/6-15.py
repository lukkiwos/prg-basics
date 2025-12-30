ean_code = input("Enter EAN-13 article number: ")

if len(ean_code) == 13:
    print("Article number is correct")
    if ean_code[0:3] == '590':
        print("Article manufactured in Poland")
else:
    print("INVALID article number")

print()





def f(ean_code):
    if len(ean_code) == 13:
        print("Article number is correct")
        if ean_code[0:3] == "590":
            return "Article manufactured in Poland"
    else:
        return "Wrong number"



if __name__ == "__main__":
    print(f('5901230094938'))