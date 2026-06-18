"""Section 6 - Integrative project: ClearContacts v1.0 (Level 1 - MVP).

TD/TP Python - Basics & Best Practices - Client Abellis - Juin 2026
Trainer : Mr. Ali ZAINOUL - CrystalClearCode (https://clearcode.fr)

Command-line contact manager combining everything covered in the two-day
session: I/O, control flow, functions, data structures and exceptions.

Data model: a contact is a dict[str, str] with keys "first_name",
"last_name", "phone" and "email". The address book itself is a
list[dict[str, str]] kept in memory, wrapped by the ContactBook class
below for a clean, testable separation between data and CLI concerns.
"""

Contact = dict[str, str]


class ContactBook:
    """In-memory address book storing contacts as a list of dicts."""

    REQUIRED_FIELDS: tuple[str, ...] = ("first_name", "last_name", "phone", "email")

    def __init__(self) -> None:
        self._contacts: list[Contact] = []

    def add(self, first_name: str, last_name: str, phone: str, email: str) -> None:
        """Add a new contact to the address book.

        Args:
            first_name: Contact's first name.
            last_name: Contact's last name.
            phone: Contact's phone number.
            email: Contact's email address.
        """
        self._contacts.append({
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone,
            "email": email,
        })

    def list_all(self) -> list[Contact]:
        """Return every contact currently stored, in insertion order."""
        return list(self._contacts)

    def search(self, query: str) -> list[Contact]:
        """Return contacts whose first or last name contains query (case-insensitive).

        Args:
            query: Search fragment.

        Returns:
            The matching contacts, in their original order.
        """
        query_lower: str = query.lower()
        return [
            c for c in self._contacts
            if query_lower in c["first_name"].lower() or query_lower in c["last_name"].lower()
        ]

    def delete(self, index: int) -> bool:
        """Delete the contact at the given 0-based index.

        Args:
            index: Position of the contact to remove, as shown by list_all().

        Returns:
            True if a contact was removed, False if the index was out of range.
        """
        if 0 <= index < len(self._contacts):
            del self._contacts[index]
            return True
        return False

    def __len__(self) -> int:
        """Return the number of contacts currently stored."""
        return len(self._contacts)


def _print_contacts(contacts: list[Contact]) -> None:
    """Display a numbered list of contacts, or a placeholder if empty."""
    if not contacts:
        print("No contacts to display.")
        return
    for i, c in enumerate(contacts):
        print(f"[{i}] {c['first_name']} {c['last_name']} - {c['phone']} - {c['email']}")


def run() -> None:
    """Launch the interactive ClearContacts menu loop.

    Menu dispatch uses structural pattern matching (`match`/`case`) instead
    of an if/elif chain. All user-input exceptions (invalid index,
    malformed input) are caught locally so the program never crashes on
    bad input.
    """
    book = ContactBook()
    menu: str = (
        "\n--- ClearContacts v1.0 ---\n"
        "1) Add a contact\n"
        "2) List contacts\n"
        "3) Search a contact\n"
        "4) Delete a contact\n"
        "5) Quit\n> "
    )

    while True:
        choice: str = input(menu).strip()

        try:
            match choice:
                case "1":
                    book.add(
                        input("First name: ").strip(),
                        input("Last name: ").strip(),
                        input("Phone: ").strip(),
                        input("Email: ").strip(),
                    )
                    print("Contact added.")
                case "2":
                    _print_contacts(book.list_all())
                case "3":
                    _print_contacts(book.search(input("Search: ").strip()))
                case "4":
                    index: int = int(input("Index to delete: "))
                    print("Deleted." if book.delete(index) else "Invalid index.")
                case "5":
                    print("Goodbye.")
                    break
                case _:
                    print("Invalid choice.")
        except ValueError as e:
            print(f"Invalid input: {e}")


if __name__ == "__main__":
    run()