import text

input_text = input("Wprowadź dowolny tekst: ")
input_letter = input("Wprowadź literę do zliczenia: ")

count = text.count_letters(input_text, input_letter)

print(f"Litera {input_letter} występuje w tekście {count} razy.")