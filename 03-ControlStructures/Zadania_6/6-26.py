def pin_verification_system():
    # Dane konfiguracyjne
    CORRECT_PIN = "0805"
    MAX_ATTEMPTS = 3
    
    print("\n --- PIN Verification System ---")
    
    # Flaga do śledzenia, czy PIN został poprawnie wprowadzony
    pin_correctly_entered = False
    
    # Pętla for do kontrolowania liczby prób (od 1 do MAX_ATTEMPTS)
    for attempt in range(1, MAX_ATTEMPTS + 1):
        
        # Wprowadzanie PIN-u
        entered_pin = input(f"Enter the PIN code: ")
        
        # Sprawdzanie poprawności PIN-u
        if entered_pin == CORRECT_PIN:
            print("\nCorrect!")
            pin_correctly_entered = True
            break # Przerywamy pętlę, jeśli PIN jest poprawny
        else:
            # Komunikat o niepowodzeniu
            print("Incorrect...")
            
    # Po wyjściu z pętli, sprawdzamy, dlaczego się zakończyła
    if not pin_correctly_entered:
        # Ten kod jest wykonywany tylko wtedy, gdy pętla zakończyła się,
        # ponieważ wyczerpano wszystkie próby (nie użyto instrukcji 'break').
        print("\nSorry, your payment card has been blocked.")

# Uruchomienie programu
# W celu demonstracji działania, należy uruchomić program i wprowadzić 3 różne PINy,
# aby zobaczyć komunikat o zablokowaniu karty.
pin_verification_system()