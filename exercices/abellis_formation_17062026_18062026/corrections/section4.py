"""Section 4 - Structures de données (str, list, tuple, dict, set).

TD/TP Python - Basics & Best Practices - Client Abellis - Juin 2026
Trainer : Mr. Ali ZAINOUL - CrystalClearCode (https://clearcode.fr)

Reference solutions for exercises 4.1 to 4.8.
"""

import random
import re

# --------------------------------------------------------------------------- #
# 4.1 - Strings (str)
# --------------------------------------------------------------------------- #

_VOWELS: frozenset[str] = frozenset("aeiouyAEIOUY")


def analyze_text(sentence: str) -> dict[str, object]:
    """Analyze a sentence: word/vowel/consonant counts and palindrome check.

    Args:
        sentence: The input sentence.

    Returns:
        A dict with 'words', 'vowels', 'consonants' and 'is_palindrome'.
    """
    letters: list[str] = [c for c in sentence if c.isalpha()]
    vowels: int = sum(1 for c in letters if c in _VOWELS)
    normalized: str = "".join(c.lower() for c in sentence if c.isalnum())

    return {
        "words": len(sentence.split()),
        "vowels": vowels,
        "consonants": len(letters) - vowels,
        "is_palindrome": normalized == normalized[::-1],
    }


def capitalize_words(sentence: str) -> str:
    """Capitalize the first letter of each word, without using str.title()."""
    return " ".join(word[:1].upper() + word[1:] for word in sentence.split())


def replace_word(sentence: str, target: str, replacement: str) -> str:
    """Replace every case-insensitive whole-word occurrence of target."""
    words: list[str] = sentence.split()
    return " ".join(
        replacement if word.lower() == target.lower() else word for word in words
    )


def caesar(text: str, shift: int) -> str:
    """Encrypt or decrypt text with a circular Caesar shift on letters only.

    Non-letter characters are left untouched. Calling caesar(caesar(t, k), -k)
    returns the original text.

    Args:
        text: Source text.
        shift: Number of positions to shift (negative to decrypt).

    Returns:
        The shifted text.
    """
    def shift_char(c: str) -> str:
        if not c.isalpha():
            return c
        base: int = ord("A") if c.isupper() else ord("a")
        return chr((ord(c) - base + shift) % 26 + base)

    return "".join(shift_char(c) for c in text)


# --------------------------------------------------------------------------- #
# 4.2 - Lists (list)
# --------------------------------------------------------------------------- #


def remove_duplicates_ordered(items: list[float]) -> list[float]:
    """Remove duplicates from a list while preserving first-seen order."""
    seen: set[float] = set()
    result: list[float] = list()
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def flatten(nested: list) -> list:
    """Recursively flatten an arbitrarily nested list.

    Args:
        nested: A list possibly containing other lists at any depth.

    Returns:
        A flat list with all elements in their original order.
    """
    flat: list = []
    for item in nested:
        flat.extend(flatten(item) if isinstance(item, list) else [item])
    return flat


def mean_and_stdev(values: list[float]) -> tuple[float, float]:
    """Compute the mean and population standard deviation, no external module."""
    n: int = len(values)
    mean: float = sum(values) / n
    variance: float = sum((x - mean) ** 2 for x in values) / n
    return mean, variance ** 0.5


# --------------------------------------------------------------------------- #
# 4.3 - Tuples (tuple)
# --------------------------------------------------------------------------- #

Point = tuple[float, float]


def distance(p1: Point, p2: Point) -> float:
    """Return the Euclidean distance between two 2D points."""
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


# --------------------------------------------------------------------------- #
# 4.4 - Dictionaries (dict)
# --------------------------------------------------------------------------- #


class PhoneBook:
    """A simple case-insensitive contact directory backed by an in-memory dict."""

    def __init__(self) -> None:
        self._contacts: dict[str, str] = {}

    def add(self, name: str, phone: str) -> None:
        """Add or update a contact."""
        self._contacts[name.lower()] = phone

    def find(self, name: str) -> str | None:
        """Look up a contact's phone number, case-insensitively."""
        return self._contacts.get(name.lower())

    def remove(self, name: str) -> bool:
        """Delete a contact; return True if it existed."""
        return self._contacts.pop(name.lower(), None) is not None

    def list_sorted(self) -> list[tuple[str, str]]:
        """Return all contacts sorted alphabetically by name."""
        return sorted(self._contacts.items())

    def save(self, path: str) -> None:
        """Persist the directory to a simple CSV file."""
        with open(path, "w", encoding="utf-8") as f:
            f.writelines(f"{name},{phone}\n" for name, phone in self.list_sorted())

    def load(self, path: str) -> None:
        """Load contacts from a CSV file, replacing the current directory."""
        with open(path, encoding="utf-8") as f:
            self._contacts = dict(line.strip().split(",", 1) for line in f if line.strip())


def word_frequency(text: str) -> dict[str, int]:
    """Count case-insensitive word occurrences, ignoring punctuation.

    Args:
        text: Source text.

    Returns:
        A dict mapping each lowercase word to its occurrence count.
    """
    words: list[str] = re.findall(r"[a-zàâäéèêëïîôöùûüç]+", text.lower())
    frequencies: dict[str, int] = {}
    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies


# --------------------------------------------------------------------------- #
# 4.5 - Sets (set / frozenset)
# --------------------------------------------------------------------------- #


def remove_duplicates_without_fromkeys(items: list[str]) -> list[str]:
    """Deduplicate a list preserving order, without dict.fromkeys()."""
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def count_unordered_pairs(items: list[str]) -> dict[frozenset[str], int]:
    """Count occurrences of unordered pairs of consecutive items via frozenset keys."""
    counts: dict[frozenset[str], int] = {}
    for a, b in zip(items, items[1:]):
        key: frozenset[str] = frozenset((a, b))
        counts[key] = counts.get(key, 0) + 1
    return counts


# --------------------------------------------------------------------------- #
# Exercise runners
# --------------------------------------------------------------------------- #


def exercise_4_1() -> None:
    """Ex 4.1 - Word/vowel/consonant counts, palindrome check, capitalisation."""
    sentence: str = input("Phrase : ")

    stats: dict[str, object] = analyze_text(sentence)
    print(f"Words       : {stats['words']}")
    print(f"Vowels   : {stats['vowels']}")
    print(f"Consonants  : {stats['consonants']}")
    print(f"Palindrome : {stats['is_palindrome']}")
    print(f"Capitalized : {capitalize_words(sentence)}")
    print(f"'le' -> 'the' : {replace_word(sentence, 'le', 'the')}")


def exercise_4_2() -> None:
    """Ex 4.2 - Caesar cipher; verifies that decryption restores the original text."""
    text: str = input("Text : ")
    shift: int = int(input("Shift : "))

    encrypted: str = caesar(text, shift)
    decrypted: str = caesar(encrypted, -shift)

    print(f"Encrypted   : {encrypted}")
    print(f"Decrypted : {decrypted}")
    print(f"Roundtrip OK : {decrypted == text}")


def exercise_4_3() -> None:
    """Ex 4.3 - Random list: sort copy, mean/stdev, dedup, recursive flatten."""
    numbers: list[float] = [random.randint(1, 50) for _ in range(10)]
    sorted_numbers: list[float] = sorted(numbers)  # does not mutate the original
    mean, stdev = mean_and_stdev(numbers)

    print(f"Original            : {numbers}")
    print(f"Sorted (copy)      : {sorted_numbers}")
    print(f"Mean                : {mean:.2f}")
    print(f"Standard deviation  : {stdev:.2f}")
    print(f"Unique              : {remove_duplicates_ordered(numbers)}")
    print(f"Flatten             : {flatten([[1, 2], [3, [4, 5]], [6]])}")


def exercise_4_4() -> None:
    """Ex 4.4 - Three list comprehensions: odd squares, identity matrix, word lengths."""
    odd_square_numbers: list[int] = [n for n in range(1, 101) if (n ** 2) % 2 == 1]
    identity_matrix: list[list[int]] = [
        [1 if row == col else 0 for col in range(5)] for row in range(5)
    ]
    sentence: str = "Python is an elegant and strong programming language"
    word_lengths: list[int] = [len(w) for w in sentence.split() if len(w) > 1]

    print(f"Squared odds (1-100)        : {odd_square_numbers}")
    print(f"Identity Matrix 5x5          : {identity_matrix}")
    print(f"Lengths (without monosyllabs) : {word_lengths}")


def exercise_4_5() -> None:
    """Ex 4.5 - Sort 2D points by distance from the origin; report the extremes."""
    points: list[Point] = [(3.0, 4.0), (1.0, 1.0), (-2.0, 5.0), (0.0, 0.0), (6.0, -1.0)]
    origin: Point = (0.0, 0.0)

    by_distance: list[Point] = sorted(points, key=lambda p: distance(p, origin))

    print(f"Sorted by distance : {by_distance}")
    print(f"The nearest        : {by_distance[0]}")
    print(f"The farthest       : {by_distance[-1]}")


def exercise_4_6() -> None:
    """Ex 4.6 - Phone book: add, find, remove, sorted listing, CSV save/load."""
    book = PhoneBook()
    book.add("Alice Dupont", "06 11 22 33 44")
    book.add("Bob Martin", "06 55 66 77 88")

    print(f"Search for 'bob martin' : {book.find('bob martin')}")
    print(f"Sorted Annuary          : {book.list_sorted()}")
    print(f"Deletion of Alice      : {book.remove('Alice Dupont')}")

    csv_path: str = "/tmp/clearcontacts_annuaire.csv"
    book.save(csv_path)
    book.load(csv_path)
    print(f"Dumped from CSV    : {book.list_sorted()}")


def exercise_4_7() -> None:
    """Ex 4.7 - Word frequency count and display of the top 5 results in a sample text."""
    text: str = (
        "Python is a powerful programming language. Python is also "
        "easy to learn. Many data scientists use Python."
    )
    frequencies: dict[str, int] = word_frequency(text)
    top_5: list[tuple[str, int]] = sorted(
        frequencies.items(), key=lambda item: item[1], reverse=True
    )[:5]

    for word, count in top_5:
        print(f"{word:<15}{count}")


def exercise_4_8() -> None:
    """Ex 4.8 - Set operations, ordered deduplication, and unordered pair counting using frozenset keys."""
    all_students: set[str] = {"Alice", "Bob", "Chloé", "David", "Emma", "Farid"}
    math_course: set[str] = {"Alice", "Bob", "Chloé"}
    physics_course: set[str] = {"Bob", "Chloé", "David"}

    print(f"Enrolled in both courses  : {math_course & physics_course}")
    print(f"Enrolled in only one course: {math_course ^ physics_course}")
    print(f"Absent from both courses   : {all_students - (math_course | physics_course)}")

    raw_items: list[str] = ["a", "b", "a", "c", "b", "d"]
    print(f"Deduplicated (order preserved)     : {remove_duplicates_without_fromkeys(raw_items)}")

    pairs_source: list[str] = ["a", "b", "a", "b", "c", "a"]
    print(f"Counting unordered pairs            : {count_unordered_pairs(pairs_source)}")


def main() -> None:
    """Run every Section 4 exercise sequentially with a clear header per exercise."""
    exercises = (
        exercise_4_1, exercise_4_2, exercise_4_3, exercise_4_4,
        exercise_4_5, exercise_4_6, exercise_4_7, exercise_4_8,
    )
    for exercise in exercises:
        print(f"\n{'=' * 60}\n{exercise.__doc__}\n{'=' * 60}")
        exercise()


if __name__ == "__main__":
    main()