N = int(input("Enter number of prime numbers to find: "))
count = 0
number = 2

print("Prime numbers: ", end=' ')

while count < N:
    prime = True
    for x in range(2, number):
        if number % x == 0:
            prime = False
            break
    if prime:
        count += 1
        print(number, end=' ')
    number += 1
