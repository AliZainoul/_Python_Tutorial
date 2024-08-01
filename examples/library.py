def print_line(s) -> None:
    print("\n"+ "-"*18 + s + "-"*18)

books = {
    "Les Misérables" :{
        "author": "Victor Hugo",
        "year": 1862},
    "L'Étranger" :{
        "author": "Albert Camus",
        "year": 1942},
    "Madame Bovary" : {
        "author": "Gustave Flaubert",
        "year": 1857},
    "À la recherche du temps perdu": {
        "author": "Marcel Proust",
        "year": 1913},
    "Le Petit Prince" : {
        "author": "Antoine de Saint-Exupéry",
        "year": 1943},
    "Germinal" : {
        "author": "Émile Zola",
        "year": 1885}
}

def print_books(books):
    for book in books:
        print(f"{book}, {books[f'{book}']}")

def available_books(books):
    for book_name, book_name_specs in books.items():
        yield book_name, book_name_specs

# def find_book(library, book_name: str):
#     if (library.get(book_name, None)):
#         print(f"Found book : {book_name} --> {library[f'{book_name}']}")
# find_book(books, "Les Misérables")
# find_book(books, "Les ")

def add_book(library, book_name) -> None:
    if is_present(library, book_name):
        print(f"The {book_name} is already present in library.")
    else:
        book_specs = dict()
        book_specs['author'] = input(f"Please enter the author of the book {book_name} : ") 
        book_specs['year'] = input(f"Please enter the year of the book {book_name} : ") 
        library[book_name] = book_specs
        print(f"{book_name} was successfully added to library: {library[book_name]}")

def find_book(library, book_name: str):
    return (library.get(book_name, "Not found"))

def is_present(library, book_name: str) -> bool:
    return bool(library.get(book_name, False))

def remove_book(library, book_name):
    return library.pop(book_name, "Book not found.")


if __name__ == "__main__":
    print_line("Printing Books initially: ")
    for book in available_books(books):
        print(book)

    a_book="Harry Potter"
    print_line(f"Adding book: {a_book}")
    add_book(books, a_book)

    print_line(f"Printing Books after adding book: {a_book}")
    for book in available_books(books):
        print(book)

    target_book = "Les Misérables"
    print_line(f"Searching book : {target_book}")
    print(find_book(books, target_book))

    target_book = "Les"
    print_line(f"Searching book : {target_book}")
    print(find_book(books, target_book))

    book_to_delete = "Harry Potter"
    print_line(f"Deleting book : {book_to_delete}")
    print(remove_book(books, book_to_delete))
    for book in available_books(books):
        print(book)

    book_to_delete = "x"
    print_line(f"Tempting to delete book : {book_to_delete}")
    print(remove_book(books, book_to_delete))