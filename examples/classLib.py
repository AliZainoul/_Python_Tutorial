from typing import Dict

def print_line(s) -> None:
    print("\n"+ "-"*18 + s + "-"*18)

class Book:
    def __init__(self, book_name: str, book_name_specs: Dict[str, int]):
        self.book_name = book_name
        self.book_name_specs = book_name_specs

class Library:
    def __init__(self, books: Dict[str, Dict[str, int]]):
        self.books = books

    def print_books(self, books):
        for book in books:
            print(f"{book}, {books[f'{book}']}")

    def available_books(self):
        for book_name, book_name_specs in self.books.items():
            print(type(self.books))
            yield book_name, book_name_specs
        

    # def find_book(library, book_name: str):
    #     if (library.get(book_name, None)):
    #         print(f"Found book : {book_name} --> {library[f'{book_name}']}")
    # find_book(books, "Les Misérables")
    # find_book(books, "Les ")

    def add_book(self, book_name) -> None:
        if self.is_present(book_name):
            print(f"The {book_name} is already present in library.")
        else:
            book_specs = dict()
            book_specs['author'] = input(f"Please enter the author of the book {book_name} : ") 
            book_specs['year'] = input(f"Please enter the year of the book {book_name} : ") 
            self.books[book_name] = book_specs
            print(f"{book_name} was successfully added to library: {self.books[book_name]}")

    def find_book(self, book_name: str):
        return (self.books.get(book_name, "Not found"))

    def is_present(self, book_name: str) -> bool:
        return bool(self.books.get(book_name, False))

    def remove_book(self, book_name):
        return self.books.pop(book_name, "Book not found.")


if __name__ == "__main__":
    list_of_books = [
        Book("Les Misérables", {"author": "Victor Hugo", "year": 1862}),
        Book("L'Étranger", {"author": "Albert Camus", "year": 1942}),
        Book("Madame Bovary", {"author": "Gustave Flaubert", "year": 1857}),
        Book("À la recherche du temps perdu", {"author": "Marcel Proust", "year": 1913}),
        Book("Le Petit Prince", {"author": "Antoine de Saint-Exupéry", "year": 1943}),
        Book("Germinal", {"author": "Émile Zola", "year": 1885})
        ]
    
    # Comprehension Dict
    books = {book.book_name: book.book_name_specs for book in list_of_books}
    # Equivalent to:
    #     books = dict()
    # for book in list_of_books:
    #     books[book.book_name] = book.book_name_specs

        
    print(type(books))
    l = Library(books)
    print_line("Printing Books initially: ")
    for book in l.available_books():
        print(book)

    a_book="Harry Potter"
    print_line(f"Adding book: {a_book}")
    l.add_book(a_book)

    print_line(f"Printing Books after adding book: {a_book}")
    for book in l.available_books():
        print(book)

    target_book = "Les Misérables"
    print_line(f"Searching book : {target_book}")
    print(l.find_book(target_book))

    target_book = "Les"
    print_line(f"Searching book : {target_book}")
    print(l.find_book(target_book))

    book_to_delete = "Harry Potter"
    print_line(f"Deleting book : {book_to_delete}")
    print(l.remove_book(book_to_delete))
    for book in l.available_books():
        print(book)

    book_to_delete = "x"
    print_line(f"Tempting to delete book : {book_to_delete}")
    print(l.remove_book(book_to_delete))
