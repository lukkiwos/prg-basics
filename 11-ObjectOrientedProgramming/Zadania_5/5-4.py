class EBook:
    def __init__(self, title, author, total_pages):
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.is_open = False
        self.current_page = 1

    def open(self):
        self.is_open = True
        print(f"The book {self.title} is now open")

    def close(self):
        self.is_open = False
        print(f"The book {self.title} is now closed")

    def next_page(self):
        if not self.is_open:
            print("Cannot turn page. The book is closed")
            return
        
        if self.current_page < self.total_pages:
            self.current_page += 1
        else:
            print("You are already at the last page.")

    def prevoius_page(self):
        if not self.is_open:
            print("Cannot turn page. The book is closed")
            return
        
        if self.current_page > 1:
            self.current_page -= 1
        else:
            print("You are already at the first page.")

    def display_info(self):
        status = "open" if self.is_open else "closed"
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Total pages: {self.total_pages}")
        print(f"Current page: {self.current_page}")
        print(f"Status: {status}")
        print("-" * 30)


def main():
    my_book = EBook("Python Programming", "John Smith", 250)

    my_book.display_info()

    my_book.open()
    my_book.display_info()

    my_book.next_page()
    my_book.next_page()
    my_book.next_page()
    my_book.display_info()

    my_book.prevoius_page()
    my_book.display_info()

    my_book.close()
    my_book.display_info()

    my_book.next_page()
    my_book.prevoius_page()


if __name__ == "__main__":
    main()
