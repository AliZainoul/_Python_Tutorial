import json
from typing import Dict

def print_line(s: str) -> None:
    """
    Prints a formatted line with a given string centered within dashes.
    
    Args:
    s (str): The string to be printed within the line.
    """
    print("\n" + "-" * 12 + s + "-" * 12)

# BEGIN CLASS LIBRARY
class Library:
    """
    Represents a library containing a collection of books.
    """

    def __init__(self, books: Dict[str, Dict[str, int]]):
        """
        Initializes a Library instance.
        
        Args:
        books (Dict[str, Dict[str, int]]): A dictionary of books with their specifications.
        """
        self.books = books

    def print_books(self, books: Dict[str, Dict[str, int]]) -> None:
        """
        Prints all books in the given dictionary.
        
        Args:
        books (Dict[str, Dict[str, int]]): A dictionary of books to be printed.
        """
        for book in books:
            print(f"{book}, {books[book]}")

    def available_books(self):
        """
        Yields the available books in the library.
        
        Yields:
        Tuple[str, Dict[str, int]]: The name and specifications of each book.
        """
        for book_name, book_name_specs in self.books.items():
            yield book_name, book_name_specs

    def add_book(self, book_name: str) -> None:
        """
        Adds a new book to the library.
        
        Args:
        book_name (str): The name of the book to be added.
        """
        if self.is_present(book_name):
            print(f"The {book_name} is already present in library.")
        else:
            book_specs = dict()
            book_specs['author'] = input(f"Please enter the author of the book {book_name} : ")
            book_specs['year'] = input(f"Please enter the year of the book {book_name} : ")
            self.books[book_name] = book_specs
            print(f"{book_name} was successfully added to library: {self.books[book_name]}")

    def find_book(self, book_name: str):
        """
        Finds a book in the library by its name.
        
        Args:
        book_name (str): The name of the book to find.
        
        Returns:
        Dict[str, int] or str: The specifications of the book if found, otherwise "Not found".
        """
        return self.books.get(book_name, "Not found")

    def is_present(self, book_name: str) -> bool:
        """
        Checks if a book is present in the library.
        
        Args:
        book_name (str): The name of the book to check.
        
        Returns:
        bool: True if the book is present, otherwise False.
        """
        return book_name in self.books

    def remove_book(self, book_name: str):
        """
        Removes a book from the library by its name.
        
        Args:
        book_name (str): The name of the book to remove.
        
        Returns:
        Dict[str, int] or str: The specifications of the removed book if found, otherwise "Book not found."
        """
        return self.books.pop(book_name, "Book not found.")

    @classmethod
    def load_books(cls, json_data: Dict[str, Dict[str, int]]):
        """
        Loads books from a given JSON data.
        
        Args:
        json_data (Dict[str, Dict[str, int]]): The JSON data containing book details.
        
        Yields:
        Tuple[str, Dict[str, int]]: The name and specifications of each book.
        """
        for name, details in json_data.items():
            yield name, details
# END CLASS LIBRARY

# BEGIN MAIN
if __name__ == "__main__":
    # Replace file_path variable with the actual json path 
    # file_path = r"C:\Users\user\Documents\cours_python\cours4-poo\td\livre.json"
    file_path = r"books.json"

    with open(file_path, 'r') as file:
        json_data = json.load(file)
    
    # Comprehension Dict
    books = {book_name: book_name_specs for book_name, book_name_specs in Library.load_books(json_data)}
    # Equivalent to:
    # books = dict()
    # for book in list_of_books:
    # books[book.book_name] = book.book_name_specs

    l = Library(books)
    print_line("Printing Books initially: ")
    for book in l.available_books():
        print(book)

    a_book = "Harry Potter"
    print_line(f"Adding book: {a_book}")
    l.add_book(a_book)

    print_line(f"Printing Books after adding book: {a_book}")
    for book in l.available_books():
        print(book)

    target_book = "Stories"
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
    print_line(f"Trying to delete book : {book_to_delete}")
    print(l.remove_book(book_to_delete))
# END MAIN
