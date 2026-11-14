def f(n):
    znalezione = 0
    liczba = 2

    while znalezione < n:
        prime_number = True

        for x in range(2, liczba):
            if liczba % x == 0:
                prime_number = False
                break 
        
        if prime_number:
            znalezione += 1
            if znalezione == n:
                return liczba
        liczba += 1

    

if __name__ == "__main__":
    print(f(1))
    print(f(5))