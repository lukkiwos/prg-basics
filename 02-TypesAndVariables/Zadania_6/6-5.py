###
# a program that prints a 9-digit telephone number
# entered from the keyboard as three groups of 3 digits each,
# separated by a dash character.
#

phone = input('Enter phone number: ')
result = phone[:3] + '-' + phone[3:6] + '-' + phone[6:]

print(f"Phone number: {result}")
print()

def f(numer):
    wynik = numer[:3] + '-' + numer[3:6] + '-' + numer[6:]
    return wynik

if __name__ == "__main__":
    result = '885350899'
    print(f(result))