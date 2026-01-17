translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}


word = input("Enter word to translate: ")

if word in translations:
    print(f"The word {word} means: {translations[word]}")
else:
    print("Translation is unavailable")