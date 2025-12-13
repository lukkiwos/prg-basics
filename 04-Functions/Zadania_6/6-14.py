def f(number1, number2, operator):
    if operator == "+":
        return number1 + number2
    
    elif operator == "-":
        return number1 - number2
    
    elif operator == "*":
        return number1 * number2
    
    elif operator == "%":
        if number2 == 0:
            return "Error"
        return number1 % number2
    
    elif operator == "**":
        return number1 ** number2
    
# --- Przykłady użycia ---

# Dodawanie (Zgodnie z Sample result: 5)
print(f(2, 3, '+'))
print(f(2, 3, '%'))
print(f(2, 3, '**'))
print(f(2, 3, '*'))
print(f(2, 3, '-'))