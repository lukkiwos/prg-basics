N = int(input("Enter the number of leading prime numbers: "))
count = 0
num = 2

while count < N:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
        count += 1
    num += 1

print()
print()




def f(N):
    count = 0
    num = 2
    lista = []

    while count < N:
        is_prime = True
        
        for i in range(2, num):
            
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime:
            lista.append(num) 
            count += 1        
        
        num += 1

    return f"Prime numbers: {lista}"


if __name__ == "__main__":
    for line in f(7):
        print(line, end="")

    print()
    print()





def f1(number):
    count = 0
    num = 2

    while count < number:
        is_prime = True
        
        for i in range(2, num):
            if num %  i == 0:
                is_prime = False
                break
        
        if is_prime:
            print(num, end=" ")
            count += 1
        
        num += 1



if __name__ == "__main__":
    print(f1(10))