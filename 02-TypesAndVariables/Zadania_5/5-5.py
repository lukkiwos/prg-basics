price = float(input("Enter price: "))
discount = float(input("Enter discount %: "))

discounted_price = price - (price * discount / 100)
difference = price - discounted_price

print(f"Price with discount: {discounted_price:.2f}")
print(f"Reduction: {difference:.2f}")
print()




def f(cena, znizka):
    po_znizce = cena - (cena * znizka / 100)
    roznica = cena - po_znizce
    return po_znizce, roznica

if __name__ == "__main__":
    print(f(24.72, 15)) # :.2f