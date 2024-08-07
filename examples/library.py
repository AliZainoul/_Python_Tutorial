def print_line(s: str) -> None:
    """
    Prints a separation line with the given text.
    
    Args:
    s (str): The text to include in the separation line.
    
    Returns:
    None
    """
    print("\n" + "-" * 12 + s + "-" * 12)

books = {
    "Les Misérables": {
        "author": "Victor Hugo",
        "year": 1862
    },
    "L'Étranger": {
        "author": "Albert Camus",
        "year": 1942
    },
    "Madame Bovary": {
        "author": "Gustave Flaubert",
        "year": 1857
    },
    "À la recherche du temps perdu": {
        "author": "Marcel Proust",
        "year": 1913
    },
    "Le Petit Prince": {
        "author": "Antoine de Saint-Exupéry",
        "year": 1943
    },
    "Germinal": {
        "author": "Émile Zola",
        "year": 1885
    }
}

def print_books(books: dict) -> None:
    """
    Prints all the books in the library.
    
    Args:
    books (dict): A dictionary of books with their details.
    
    Returns:
    None
    """
    for book in books:
        print(f"{book}, {books[f'{book}']}")

def available_books(books: dict):
    """
    Yields the available books and their details in the library.
    
    Args:
    books (dict): A dictionary of books with their details.
    
    Yields:
    tuple: A tuple containing the book name and its details.
    """
    for book_name, book_name_specs in books.items():
        yield book_name, book_name_specs

def add_book(library: dict, book_name: str) -> None:
    """
    Adds a new book to the library if it is not already present.
    
    Args:
    library (dict): The library dictionary.
    book_name (str): The name of the book to add.
    
    Returns:
    None
    """
    if is_present(library, book_name):
        print(f"The {book_name} is already present in library.")
    else:
        book_specs = dict()
        book_specs['author'] = input(f"Please enter the author of the book {book_name}: ")
        book_specs['year'] = input(f"Please enter the year of the book {book_name}: ")
        library[book_name] = book_specs
        print(f"{book_name} was successfully added to library: {library[book_name]}")

def find_book(library: dict, book_name: str):
    """
    Finds a book in the library by its name.
    
    Args:
    library (dict): The library dictionary.
    book_name (str): The name of the book to find.
    
    Returns:
    dict or str: The book details if found, otherwise "Not found".
    """
    return library.get(book_name, "Not found")

def is_present(library: dict, book_name: str) -> bool:
    """
    Checks if a book is present in the library.
    
    Args:
    library (dict): The library dictionary.
    book_name (str): The name of the book to check.
    
    Returns:
    bool: True if the book is present, False otherwise.
    """
    return bool(library.get(book_name, False))

def remove_book(library: dict, book_name: str):
    """
    Removes a book from the library.
    
    Args:
    library (dict): The library dictionary.
    book_name (str): The name of the book to remove.
    
    Returns:
    dict or str: The removed book details if found, otherwise "Book not found."
    """
    return library.pop(book_name, "Book not found.")

# BEGIN MAIN
if __name__ == "__main__":
    print_line("Printing Books initially: ")
    for book in available_books(books):
        print(book)

    a_book = "Harry Potter"
    print_line(f"Adding book: {a_book}")
    add_book(books, a_book)

    print_line(f"Printing Books after adding book: {a_book}")
    for book in available_books(books):
        print(book)

    target_book = "Les Misérables"
    print_line(f"Searching book: {target_book}")
    print(find_book(books, target_book))

    target_book = "Les"
    print_line(f"Searching book: {target_book}")
    print(find_book(books, target_book))

    book_to_delete = "Harry Potter"
    print_line(f"Deleting book: {book_to_delete}")
    print(remove_book(books, book_to_delete))
    for book in available_books(books):
        print(book)

    book_to_delete = "x"
    print_line(f"Tempting to delete book: {book_to_delete}")
    print(remove_book(books, book_to_delete))
# END MAIN
