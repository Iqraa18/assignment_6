# book.py

class Book:
    total_books = 0  # class variable

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def show_total_books(cls):
        print("Total books:", cls.total_books)

# Example usage
b1 = Book("Python 101")
b2 = Book("OOP in Practice")

Book.show_total_books()
