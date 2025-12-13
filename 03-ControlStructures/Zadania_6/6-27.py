for i in range(6,-1,-3):
    for j in range(1,4):
        print(f'{i+j}',end=' ')
    print()


# Inicjalizacja pętli zewnętrznej (odpowiednik for i in range(0, -3, -1))
i = 0
while i > -3:
    
    # Inicjalizacja pętli wewnętrznej (odpowiednik for j in range(1, 4))
    j = 1
    while j < 4:
        
        # Logika drukowania wartości pozostaje bez zmian
        # j: 1, 2, 3
        # i: 0, -1, -2
        print(f'{j + (i * -3)}', end='')
        
        # Zmiana wartości licznika pętli wewnętrznej (j += 1)
        j += 1
        
    # Przejście do nowej linii po zakończeniu wiersza
    print()
    
    # Zmiana wartości licznika pętli zewnętrznej (i -= 1)
    i -= 1