###
# A simple number guessing game
#
import random

# Randomly chosen number to be guessed from 1 to 100
number_to_guess = random.randint(1, 100)
user_guess = 0

print("Guess the number between 1 and 100!")

while user_guess != number_to_guess:
    user_guess = int(input("Enter your guess: "))

    if user_guess < number_to_guess:
        print("Too low! Try again.")
    elif user_guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number.")
print()



def f():
    import random
    
    number_to_guess = random.randint(1, 100)
    user_guess = 0
    
    print("Zgadnij liczbę pomiędzy 1 a 100!")

    while user_guess != number_to_guess:
        user_guess = int(input("Wprowadź liczbę do zgadnięcia: "))
        
        if user_guess > number_to_guess:
            print("Za wysoko! Próbuj dalej")
        elif user_guess < number_to_guess:
            print("Za nisko! Próbuj dalej")
        else:
            return "Gratulację zgadłeś liczbę!"
        

if __name__ == "__main__":
    print(f())