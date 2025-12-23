###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print(f'Number of characters: {len(movie)}')
print()

# print title in capital letters
print(f"Title in capital letters: {movie.upper()}")
print()

# print title in small letters
print(f"Title in small letters: {movie.casefold()}")
print()

# print how many times the vowel "e" appears in the title
print(f"How many times vowel 'e' appears: {movie.count('e')}")
print()

# print where in the text is the word "Lord"
print(f"Where in the text is word 'Lord': {movie.find('Lord')}")
print()

# print where in the text is the word "dragon"
print(f"Where in the text is word 'dragon': {movie.find('dragon')}")
print()
print()
print()
print()


def f_len(movie):           # 1
    return len(movie)

def f_capital(movie):       # 2
    return movie.upper()

def f_small(movie):         # 3
    return movie.casefold()

def f_e(movie):             # 4
    return movie.count('e')

def f_lord(movie):          # 5
    return movie.find('Lord')

def f_dragon(movie):        # 6
    return movie.find('dragon')

if __name__ == "__main__":
    film = "The Lord of the Rings: The Return of the King"
    print(f_len(film))
    print(f_capital(film))
    print(f_small(film))
    print(f_e(film))
    print(f_lord(film))
    print(f_dragon(film))