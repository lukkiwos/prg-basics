import csv

# mapowanie gatunku na nazwę pliku
genre_files = {
    "Fantasy": "books_fantasy.txt",
    "Historical": "books_historical.txt",
    "Romance": "books_romance.txt",
    "Classic": "books_classic.txt"
}


def get_file_for_genre(genre):
    
    return genre_files.get(genre)


def save_book_to_file(book_line, file_name):
    
    with open(file_name, 'a', encoding='utf-8') as f:
        f.write(book_line + "\n")


def process_books(csv_file):
    
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)  # pomijamy nagłówek

        for row in reader:
            title = row[0]
            author = row[1]
            genre = row[2]
            year = row[3]

            file_name = get_file_for_genre(genre)
            if file_name:
                # tworzymy linię do zapisu w pliku
                line_to_save = f"{title},{author},{genre},{year}"
                save_book_to_file(line_to_save, file_name)


# uruchomienie programu
process_books("books.csv")
print("Books copied to genre files successfully.")