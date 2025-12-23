amount_str = input("Amount: ")
amount = float(amount_str)
vat = amount * 0.23
without_vat = amount - vat

print(f"Vat 23%: {vat:.2f}")
print(f"Without Vat 23%: {without_vat:.2f}")
print()



def f(cena, vat):
    sam_vat = cena * vat
    bez_vatu = cena - sam_vat
    return sam_vat, bez_vatu

if __name__ == "__main__":
    print(f"{f(15.84, 0.23)}")     # :.2f ?