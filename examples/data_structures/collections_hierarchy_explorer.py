#!/usr/bin/env python3
"""
Collections Hierarchy Explorer
==============================

This module explores Python's collections type hierarchy, displaying:
- Abstract Base Classes (ABCs) from collections.abc
- Concrete built-in types (tuple, list, dict, set, etc.)
- Collections module specialized containers (deque, Counter, etc.)

The script visualizes the Method Resolution Order (MRO) for each type,
color-coded by mutability:
- RED: Immutable types (cannot be modified after creation)
- DARK_GREEN: Mutable types (can be modified in place)
- BLUE: Abstract base classes (cannot be instantiated directly)

Author: Collections Type System Explorer
Date: 2025-11-01
"""

from collections import (
    deque,
    Counter,
    OrderedDict,
    defaultdict,
    ChainMap,
    UserDict,
    UserList,
    UserString,
    namedtuple
)

from collections.abc import (
    Iterable,
    Iterator,
    Reversible,
    Collection,
    Sequence,
    MutableSequence,
    Set,
    MutableSet,
    Mapping,
    MutableMapping,
    ByteString,
    Sized,
    Container
)

from typing import Type, List, Tuple
import types


# ANSI Color codes
class Colors:
    """ANSI color codes for terminal output."""
    RED = '\033[91m'            # Immutable types
    DARK_GREEN = '\033[32m'     # Mutable types
    BLUE = '\033[94m'           # Abstract base classes
    CYAN = '\033[96m'           # HEADERS and Section titles
    MAGENTA = '\033[95m'        # Special emphasis
    BOLD = '\033[1m'            # Bold text
    UNDERLINE = '\033[4m'       # Underlined text
    RESET = '\033[0m'           # Reset to default
    DARK_BLUE = '\033[34m'      # Additional color

def print_header(text: str, char: str = "=") -> None:
    """
    Print a formatted header with colors.
    
    Args:
        text: Header text to display
        char: Character to use for the border line
    """
    border = char * 80
    print(f"\n{Colors.BOLD}{Colors.BOLD}{border}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BOLD}{text:^80}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BOLD}{border}{Colors.RESET}\n")


def print_mro_table(class_name: str, mro: Tuple[Type, ...], color: str, 
                    mutability: str, description: str = "") -> None:
    """
    Print a formatted table showing the Method Resolution Order for a class.
    
    Args:
        class_name: Name of the class
        mro: Tuple of classes in the MRO
        color: ANSI color code for the class name
        mutability: "Immutable", "Mutable", or "Abstract"
        description: Optional description of the class
    """
    # Header
    print(f"{color}{Colors.BOLD}┌{'─' * 78}┐{Colors.RESET}")
    print(f"{color}{Colors.BOLD}│ {class_name:<76} │{Colors.RESET}")
    print(f"{color}│ {mutability:<76} │{Colors.RESET}")
    
    if description:
        # Wrap description if too long
        max_len = 76
        words = description.split()
        lines = []
        current_line = []
        current_length = 0
        
        for word in words:
            if current_length + len(word) + 1 <= max_len:
                current_line.append(word)
                current_length += len(word) + 1
            else:
                lines.append(' '.join(current_line))
                current_line = [word]
                current_length = len(word)
        
        if current_line:
            lines.append(' '.join(current_line))
        
        for line in lines:
            print(f"{color}│ {line:<76} │{Colors.RESET}")
    
    print(f"{color}├{'─' * 78}┤{Colors.RESET}")
    print(f"{color}│ {'MRO (Method Resolution Order):':<76} │{Colors.RESET}")
    print(f"{color}├{'─' * 78}┤{Colors.RESET}")
    
    # MRO chain
    for i, cls in enumerate(mro):
        arrow = "  ↓  " if i < len(mro) - 1 else "     "
        class_repr = f"{i+1}. {cls.__module__}.{cls.__name__}" if hasattr(cls, '__module__') else f"{i+1}. {cls.__name__}"
        print(f"{color}│ {class_repr:<76} │{Colors.RESET}")
        if arrow.strip():
            print(f"{color}│ {arrow:^76} │{Colors.RESET}")
    
    print(f"{color}{Colors.BOLD}└{'─' * 78}┘{Colors.RESET}\n")


def explore_abstract_base_classes() -> None:
    """Explore and display all Abstract Base Classes from collections.abc."""
    print_header("ABSTRACT BASE CLASSES (collections.abc)", "=")
    
    abcs = [
        (Iterable, "Base for all iterable objects (supports __iter__)"),
        (Iterator, "Objects that produce values one at a time (supports __iter__ and __next__)"),
        (Reversible, "Iterables that can be reversed (supports __reversed__)"),
        (Collection, "Sized iterable containers (combines Sized, Iterable, Container)"),
        (Sequence, "Ordered collections with indexed access (tuple, list, str, etc.)"),
        (MutableSequence, "Sequences that can be modified (list, deque, bytearray)"),
        (ByteString, "Sequences of bytes (bytes, bytearray) - deprecated in Python 3.12+"),
        (Set, "Unordered collections of unique elements (frozenset, set)"),
        (MutableSet, "Sets that can be modified (set)"),
        (Mapping, "Collections of key-value pairs (dict, OrderedDict, etc.)"),
        (MutableMapping, "Mappings that can be modified (dict, OrderedDict, etc.)"),
        (Sized, "Objects with a length (supports __len__)"),
        (Container, "Objects that support membership testing (supports __contains__)"),
    ]
    
    for abc, description in abcs:
        print_mro_table(
            abc.__name__,
            abc.__mro__,
            Colors.BLUE,
            "Abstract Base Class (cannot be instantiated)",
            description
        )


def explore_immutable_builtins() -> None:
    """Explore and display immutable built-in types."""
    print_header("IMMUTABLE BUILT-IN TYPES", "=")
    
    immutable_types = [
        (tuple, "Ordered, immutable sequence of objects"),
        (str, "Immutable sequence of Unicode characters"),
        (bytes, "Immutable sequence of bytes (0-255)"),
        (frozenset, "Immutable set of unique, hashable objects"),
        (range, "Immutable sequence of numbers, commonly used for looping"),
        (types.MappingProxyType, "Read-only proxy of a mapping (dict)"),
    ]
    
    for cls, description in immutable_types:
        print_mro_table(
            cls.__name__,
            cls.__mro__,
            Colors.RED,
            "⛔ IMMUTABLE - Cannot be modified after creation",
            description
        )


def explore_mutable_builtins() -> None:
    """Explore and display mutable built-in types."""
    print_header("MUTABLE BUILT-IN TYPES", "=")
    
    mutable_types = [
        (list, "Ordered, mutable sequence allowing duplicates"),
        (bytearray, "Mutable sequence of bytes (0-255)"),
        (set, "Unordered, mutable collection of unique, hashable objects"),
        (dict, "Mutable mapping of key-value pairs (hash table)"),
    ]
    
    for cls, description in mutable_types:
        print_mro_table(
            cls.__name__,
            cls.__mro__,
            Colors.DARK_GREEN,
            "✓ MUTABLE - Can be modified in place",
            description
        )


def explore_collections_module() -> None:
    """Explore and display specialized containers from collections module."""
    print_header("COLLECTIONS MODULE - SPECIALIZED CONTAINERS", "=")
    
    collections_types = [
        # Mutable
        (deque, Colors.DARK_GREEN, "✓ MUTABLE", 
         "Double-ended queue with O(1) appends/pops from both ends"),
        (Counter, Colors.DARK_GREEN, "✓ MUTABLE", 
         "Dict subclass for counting hashable objects (multiset/bag)"),
        (OrderedDict, Colors.DARK_GREEN, "✓ MUTABLE", 
         "Dict that remembers insertion order (less relevant since Python 3.7+)"),
        (defaultdict, Colors.DARK_GREEN, "✓ MUTABLE", 
         "Dict with factory function for missing keys (auto-initialization)"),
        (ChainMap, Colors.DARK_GREEN, "✓ MUTABLE", 
         "Groups multiple dicts into a single view with precedence"),
        (UserDict, Colors.DARK_GREEN, "✓ MUTABLE", 
         "Wrapper around dict for easier subclassing"),
        (UserList, Colors.DARK_GREEN, "✓ MUTABLE", 
         "Wrapper around list for easier subclassing"),
        (UserString, Colors.DARK_GREEN, "✓ MUTABLE", 
         "Wrapper around str for easier subclassing (but str is immutable)"),
    ]
    
    for cls, color, mutability, description in collections_types:
        print_mro_table(cls.__name__, cls.__mro__, color, mutability, description)
    
    # Special case: namedtuple is a factory function
    print(f"{Colors.MAGENTA}{Colors.BOLD}┌{'─' * 78}┐{Colors.RESET}")
    print(f"{Colors.MAGENTA}{Colors.BOLD}│ {'namedtuple (Factory Function)':<76} │{Colors.RESET}")
    print(f"{Colors.MAGENTA}│ {'⚙️  Special: Creates new tuple subclasses dynamically':<76} │{Colors.RESET}")
    print(f"{Colors.MAGENTA}├{'─' * 78}┤{Colors.RESET}")
    print(f"{Colors.MAGENTA}│ namedtuple is not a class but a factory function that creates new      │{Colors.RESET}")
    print(f"{Colors.MAGENTA}│ classes. Each call returns a new class that inherits from tuple.       │{Colors.RESET}")
    print(f"{Colors.MAGENTA}├{'─' * 78}┤{Colors.RESET}")
    
    # Create example
    Point = namedtuple('Point', ['x', 'y'])
    print(f"{Colors.MAGENTA}│ Example: Point = namedtuple('Point', ['x', 'y'])                       │{Colors.RESET}")
    print(f"{Colors.MAGENTA}├{'─' * 78}┤{Colors.RESET}")
    print(f"{Colors.RED}│ Point MRO (inherits from tuple - IMMUTABLE):                           │{Colors.RESET}")
    print(f"{Colors.MAGENTA}├{'─' * 78}┤{Colors.RESET}")
    
    for i, cls in enumerate(Point.__mro__):
        arrow = "  ↓  " if i < len(Point.__mro__) - 1 else "     "
        class_repr = f"{i+1}. {cls.__name__}"
        print(f"{Colors.RED}│ {class_repr:<76} │{Colors.RESET}")
        if arrow.strip():
            print(f"{Colors.RED}│ {arrow:^76} │{Colors.RESET}")
    
    print(f"{Colors.MAGENTA}{Colors.BOLD}└{'─' * 78}┘{Colors.RESET}\n")


def print_summary() -> None:
    """Print a summary of Python's collection type system."""
    print_header("SUMMARY: PYTHON COLLECTIONS TYPE SYSTEM", "=")
    
    summary = f"""
{Colors.BOLD}Key Concepts:{Colors.RESET}

{Colors.BLUE}1. Abstract Base Classes (ABCs){Colors.RESET} - Define interfaces without implementation
   - Located in collections.abc module
   - Used for type checking and protocol definition
   - Cannot be instantiated directly
   - Examples: Iterable, Sequence, Mapping

{Colors.RED}2. Immutable Types{Colors.RESET} - Cannot be modified after creation
   - Hashable (can be used as dict keys or set elements)
   - Thread-safe by nature
   - Examples: tuple, str, bytes, frozenset, range

{Colors.DARK_GREEN}3. Mutable Types{Colors.RESET} - Can be modified in place
   - Not hashable (cannot be dict keys)
   - More memory efficient for modifications
   - Examples: list, dict, set, bytearray, deque

{Colors.BOLD}Method Resolution Order (MRO):{Colors.RESET}
   - Shows the inheritance chain from specific to general
   - Python uses C3 Linearization algorithm
   - Determines which method gets called in inheritance hierarchies
   - Always ends with 'object' (the base of all classes)

{Colors.BOLD}Why This Matters:{Colors.RESET}
   - Understanding the hierarchy helps choose the right data structure
   - ABCs enable duck typing and isinstance() checks
   - MRO explains method lookup and super() behavior
   - Mutability affects hashability, thread-safety, and performance
    """
    
    print(summary)


def main() -> None:
    """Main function to explore all collection types."""
    print(f"\n{Colors.BOLD}{Colors.BOLD}")
    print("╔" + "═" * 78 + "╗")
    print("║" + " " * 78 + "║")
    print("║" + "PYTHON COLLECTIONS HIERARCHY EXPLORER".center(78) + "║")
    print("║" + " " * 78 + "║")
    print("║" + "Complete Analysis of Python's Collection Type System".center(78) + "║")
    print("║" + " " * 78 + "║")
    print("╚" + "═" * 78 + "╝")
    print(Colors.RESET)
    
    explore_abstract_base_classes()
    explore_immutable_builtins()
    explore_mutable_builtins()
    explore_collections_module()
    print_summary()
    
    print(f"\n{Colors.BOLD}{Colors.BOLD}{'=' * 80}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BOLD}{'End of Collections Hierarchy Explorer':^80}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BOLD}{'=' * 80}{Colors.RESET}\n")


if __name__ == "__main__":
    main()