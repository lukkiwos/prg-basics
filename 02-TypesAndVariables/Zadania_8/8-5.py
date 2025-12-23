###
# A program that reads a SWIFT code from the keyboard
# and prints the bank code and country code.
#

swift = input('Enter a SWIFT code: ')

print(f'Bank Code: {swift[:4]}')
print(f'Country Code: {swift[4:6]}')
print()




def f(swift):
    bank_code = swift[:4]
    country_code = swift[4:6]
    swift_code = [str(bank_code), str(country_code)]
    return " ".join(swift_code)


if __name__ == "__main__":
    print(f("BPKOPLPW"))
    print(f("CHASUS33"))
    print(f("DEUTDEFF"))
