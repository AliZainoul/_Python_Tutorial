# ====================================================
# METHOD OVERLOADING --> COMPILE TIME POLYMORPHISM (parametric polymorphism via templates/ generics)
# ====================================================

from typing import TypeVar, Generic

# Define a type variable
T = TypeVar("T", int, float, str, list) # Can be extended to other types as needed

class Pair(Generic[T]):
    """
    A generic Pair class demonstrating compile-time polymorphism in Python.

    Attributes:
        first (T): The first element.
        second (T): The second element.

    Methods:
        add() -> T: Returns the sum of the elements (works for int, float, str, list, etc.)

    This mimics templates in C++ and generics in Java.

    Python equivalent of compile-time polymorphism using generics:
        Pair[int], Pair[float], Pair[str], etc.

    C++ Template Equivalent:
        template <typename T>
        class Pair {
        public:
            T first, second;
            Pair(T a, T b) : first(a), second(b) {}
            T add() { return first + second; }
        };

        Pair<int> p1(2, 3);
        std::cout << p1.add();  // 5
        Pair<std::string> p2("Hello ", "World");
        std::cout << p2.add();  // Hello World

    Java Generics Equivalent:
        public class Pair<T> {
            private T first;
            private T second;

            public Pair(T first, T second) {
                this.first = first;
                this.second = second;
            }

            public T add() {
                // Works for numeric types, strings, lists, etc. (assumes operator+ is defined)
                return first + second;
            }
        }

        Pair<Integer> p1 = new Pair<>(2, 3);
        System.out.println(p1.add());  // 5
        Pair<String> p2 = new Pair<>("Hello ", "World");
        System.out.println(p2.add());  // Hello World
    """

    def __init__(self, first: T, second: T):
        self.first: T = first
        self.second: T = second

    def add(self) -> T:
        """Returns the sum/concatenation of first and second elements."""
        return self.first + self.second

    def __repr__(self):
        return f"Pair({self.first}, {self.second})"


def main():
    print("\n" + "Demonstrating (simulated) Compile-Time Polymorphism with Generics in Python")
    print("#" * 60)
    print("Integer Pair")
    int_pair = Pair[int](2, 3)
    print(int_pair)
    print("Add:", int_pair.add())

    print("\nFloat Pair")
    float_pair = Pair[float](2.5, 3.5)
    print(float_pair)
    print("Add:", float_pair.add())

    print("\nString Pair")
    string_pair = Pair[str]("Hello ", "World")
    print(string_pair)
    print("Add:", string_pair.add())

    print("\nList Pair")
    list_pair = Pair[list]([1, 2], [3, 4])
    print(list_pair)
    print("Add:", list_pair.add())


if __name__ == "__main__":
    main()
