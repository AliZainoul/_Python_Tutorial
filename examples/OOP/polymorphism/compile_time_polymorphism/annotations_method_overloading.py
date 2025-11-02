# ====================================================
# METHOD OVERLOADING --> COMPILE TIME POLYMORPHISM
# ====================================================

# Example 1: Naive multiple static methods (overridden in Python)
class MathOperationsNaive:
    # @staticmethod
    # def add(a: int, b: int) -> int:
    #     print("Calls int add method version.")
    #     return a + b
    
    # @staticmethod
    # def add(a: float, b: float) -> float:
    #     print("Calls float add method version.")
    #     return a + b

    # @staticmethod
    # def add(a: str, b: str) -> str:
    #     print("Calls str add method version.")
    #     return a + b
    
    @staticmethod
    def add(a: list, b: list) -> list:
        print("Calls list add method version.")
        return a + b


# Note: In Python, the last defined method with the same name will override the previous ones.
# Therefore, only the last 'add' method will be effective.
# To achieve method overloading behavior, we can use type checking within a single method.
# Here's an example:

# Example 2: Proper type-checked single method
class MathOperations:
    """
    Provides a static 'add' method that demonstrates a form of compile-time
    method overloading in Python.

    Unlike languages such as C++ or Java, Python does not support true
    compile-time method overloading because it is a dynamically typed
    language. Instead, this implementation mimics method overloading
    by using type checks within a single method. Here, we simulate overloading
    using runtime type checks with isinstance().

    The 'add' method behaves differently depending on the types of
    its arguments:

    - int + int -> adds two integers
    - float + float -> adds two floats
    - str + str -> concatenates two strings
    - list + list -> concatenates two lists
    - Any other type combination raises TypeError

    Examples of equivalent compile-time overloading in other languages:

    C++:
        class MathOperations {
        public:
            int add(int a, int b) { return a + b; }
            double add(double a, double b) { return a + b; }
            std::string add(const std::string &a, const std::string &b) { return a + b; }
        };

        MathOperations mo;
        mo.add(2, 3);          // Calls int version
        mo.add(2.5, 3.5);      // Calls double version
        mo.add("Hello ", "C++"); // Calls string version

    Java:
        public class MathOperations {
            public int add(int a, int b) { return a + b; }
            public double add(double a, double b) { return a + b; }
            public String add(String a, String b) { return a + b; }
        }

        MathOperations mo = new MathOperations();
        mo.add(2, 3);          // Calls int version
        mo.add(2.5, 3.5);      // Calls double version
        mo.add("Hello ", "Java"); // Calls string version

    In Python, due to dynamic typing, the types are checked at runtime
    using `isinstance`, which simulates the compile-time method selection
    found in statically typed languages.
    """

    @staticmethod
    def add(a, b):
        match (a, b):
            case (a, b) if isinstance(a, int) and isinstance(b, int):
                print("Calls int add method version.")
                return a + b
            case (a, b) if isinstance(a, float) and isinstance(b, float):
                print("Calls float add method version.")
                return a + b
            case (a, b) if isinstance(a, str) and isinstance(b, str):
                print("Calls str add method version.")
                return a + b
            case (a, b) if isinstance(a, list) and isinstance(b, list):
                print("Calls list add method version.")
                return a + b
            case _:
                raise TypeError(f"Unsupported types for add method: {type(a)} + {type(b)}")


def main():
    print("\n")
    print("#" * 60)
    print("Example 1: Naive multiple static methods (Python overrides)")
    print("#" * 60)
    print("Test naive overloading (only last 'add' survives in Python)")
    # # Test integers
    # print(MathOperationsNaive.add(2, 3))  # Output: 5

    # # Test floats
    # print(MathOperationsNaive.add(2.5, 3.5))  # Output: 6.0

    # # Test strings
    # print(MathOperationsNaive.add("Hello ", str(input("Enter your name: "))))  # Output: Hello <Name>

    # Test lists
    print(MathOperationsNaive.add([1, 2], [3, 4]))  # Output: [1, 2, 3, 4]

    print("\n" + "#" * 60)
    print("Example 2: Proper type-checked single method")
    print("#" * 60)
    
    # Test integers
    print(MathOperations.add(2, 3))  # Output: 5

    # Test floats
    print(MathOperations.add(2.5, 3.5))  # Output: 6.0

    # Test strings
    print(MathOperations.add("Hello ", str(input("Enter your name: "))))  # Output: Hello <Name>

    # Test lists
    print(MathOperations.add([1, 2], [3, 4]))  # Output: [1, 2, 3, 4]

    # Test unsupported types (raises TypeError)
    try:
        print(MathOperations.add(2, "3"))
    except TypeError as e:
        print(e)


if __name__ == "__main__":
    main()
