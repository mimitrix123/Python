"""Week 3 Assignment 2: OOP Library Management System."""


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.issued = False

    def __str__(self):
        status = "Issued" if self.issued else "Available"
        return f"{self.title} by {self.author} - {status}"


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        if book.title in self.books:
            raise ValueError("A book with this title already exists.")
        self.books[book.title] = book

    def remove_book(self, title):
        book = self.books.get(title)
        if book is None:
            raise ValueError("Book not found.")
        if book.issued:
            raise ValueError("Issued books cannot be removed.")
        del self.books[title]

    def issue_book(self, title):
        book = self.books.get(title)
        if book is None:
            raise ValueError("Book not found.")
        if book.issued:
            raise ValueError("Book is already issued.")
        book.issued = True

    def return_book(self, title):
        book = self.books.get(title)
        if book is None:
            raise ValueError("Book not found.")
        if not book.issued:
            raise ValueError("Book is already available.")
        book.issued = False

    def show_books(self):
        for book in self.books.values():
            print(book)


def main():
    library = Library()
    library.add_book(Book("Python Basics", "A. Developer"))
    library.add_book(Book("Clean Code", "R. Martin"))
    library.issue_book("Python Basics")
    library.show_books()
    library.return_book("Python Basics")


if __name__ == "__main__":
    main()
