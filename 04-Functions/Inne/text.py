def count_letters(text, letter):
    text_lower = text.lower()
    letter_lower = letter.lower()

    count = text_lower.count(letter_lower)
    return count