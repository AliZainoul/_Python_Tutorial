"""
CRUD : Create Read Update Delete
Projet Final : Créez un programme de gestion de bibliothèque qui inclut les éléments suivants :

• Partie 1 : Définition des fonctions de base
– Créez une fonction add_book(library, book_name) qui ajoute 
un livre à la bibliothèque (représentée par un dictionnaire). (CREATE)
– Créez une fonction remove_book(library, book_name) qui supprime un livre de la bibliothèque. (DELETE)
– Créez une fonction find_book(library, book_name) qui vérifie si un livre est présent dans la bibliothèque. (READ)

• Partie 2 : Générateurs et itérateurs
– Créez un générateur available_books(library) qui génère la liste des livres disponibles dans la bibliothèque. (READ)

• Partie 3 : Gestion avancée des livres
– Utilisez des fonctions anonymes lambda avec map() pour créer une liste des noms des livres en majuscules.
– Utilisez filter() pour créer une liste des livres dont le nom commence par une lettre spécifique.

• Partie 4 : Exécution dynamique
– Utilisez eval() pour permettre à l’utilisateur de saisir une expression conditionnelle pour rechercher des livres (par ex- emple, tous les livres contenant "Python").
– Utilisez exec() pour permettre à l’utilisateur d’ajouter dy- namiquement une nouvelle fonctionnalité au programme (par exemple, ajouter une nouvelle méthode de tri pour les livres).
"""

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

def print_books(library: dict) -> None:
    """
    Prints all the books in the library.
    
    Args:
    library (dict): A dictionary of books with their details.
    
    Returns:
    None
    """
    for book_name in library:
        print(f"{book_name}, {library[f'{book_name}']}")

def available_books(library: dict):
    """
    Yields the available books and their details in the library.
    
    Args:
    library (dict): A dictionary of books with their details.
    
    Yields:
    tuple: A tuple containing the book name and its details.
    """
    for book_name, book_name_specs in library.items():
        yield book_name, book_name_specs

def print_all(library: dict) -> None:
    for book in available_books(library):
        print(book)


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
        book_specs['year'] = int(input(f"Please enter the year of the book {book_name}: "))
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

def _find_book(library: dict, prompt: str) -> list:
    """
    Finds a book in the library by its name.
    
    Args:
    library (dict): The library dictionary.
    book_name (str): The name of the book to find.
    
    Returns:
    list of books (list): All books if prompt found in book details, otherwise an empty list.
    """
    
    # l = []
    # for book_name, book_specs in library.items():
    #     if prompt in book_name:
    #         l.append((book_name, book_specs))
        
    #     book_details = list(book_specs.values())
    #     for el in book_details:
    #         if(isinstance(el, int)):
    #             if prompt in str(el):
    #                 l.append((book_name, book_specs))
    #         if(isinstance(el, str)):        
    #             if prompt in el:
    #                 l.append((book_name, book_specs))

    # return l


    # Return a list of tuples (book_name, book_specs) for books where prompt is found in book_name or any value of book_specs
    return [
        (book_name, book_specs)
        for book_name, book_specs in library.items()
        if prompt in book_name
        or any(prompt in str(el) for el in list(book_specs.values()))
    ]

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
    print_all(books)

    a_book = "Harry Potter"
    print_line(f"Adding book: {a_book}")
    add_book(books, a_book)

    print_line(f"Printing Books after adding book: {a_book}")
    print_all(books)


    target_book = "Les Misérables"
    print_line(f"Searching book: {target_book}")
    print(find_book(books, target_book))

    target_book = "Hugo"
    print_line(f"Searching book: {target_book}")
    print_line(f"with function FIND_BOOK uses get method of DICT")
    print(find_book(books, target_book))

    target_book = "Hugo"
    print_line(f"Searching book: {target_book}")
    print_line(f"with function _FIND_BOOK uses IN operator with prompt")
    print(_find_book(books, target_book))

    target_book = "2"
    print_line(f"Searching book: {target_book}")
    print_line(f"with function _FIND_BOOK uses IN operator with prompt")
    print(_find_book(books, target_book))

    target_book = input("Please enter your targeted book (as author, year or book name) : ")
    print_line(f"Searching book: {target_book}")
    print_line(f"with function _FIND_BOOK uses IN operator with prompt")
    print(_find_book(books, target_book))

    book_to_delete = "Harry Potter"
    print_line(f"Deleting book: {book_to_delete}")
    print(f"{remove_book(books, book_to_delete)} \n")
    print_all(books)

    book_to_delete = "x"
    print_line(f"Tempting to delete book: {book_to_delete}")
    print(remove_book(books, book_to_delete))
# END MAIN
