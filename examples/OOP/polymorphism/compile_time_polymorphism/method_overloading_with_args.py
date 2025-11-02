class MathOperations:
    """
    Demonstrates how Python can mimic compile-time method overloading
    (static polymorphism) using optional arguments, *args, and **kwargs.

    Techniques used:
    1. Default arguments (None) to simulate multiple signatures
    2. *args to accept variable number of positional arguments
    3. **kwargs to accept variable number of named arguments

    Examples:
        MathOperations.add(1, 2)
        MathOperations.add(1, 2, 3)
        MathOperations.add(1, 2, 3, 4)
        MathOperations.add_args(1, 2, 3)
        MathOperations.add_kwargs(a=1, b=2, c=3)

    Python mimics the behavior, but actual method selection occurs at runtime.

    C++ Equivalent:
    ----------------
    class MathOperations {
    public:
        int add(int a, int b) { return a + b; }
        int add(int a, int b, int c) { return a + b + c; }
        int add(int a, int b, int c, int d) { return a + b + c + d; }
    };

    Java Equivalent:
    ----------------
    class MathOperations {
        int add(int a, int b) { return a + b; }
        int add(int a, int b, int c) { return a + b + c; }
        int add(int a, int b, int c, int d) { return a + b + c + d; }
    }
    """

    # Example 1: Using None as default for optional parameters
    @staticmethod
    def add(a, b, c=None, d=None):
        if c is None and d is None:
            return a + b
        elif d is None:
            return a + b + c
        else:
            return a + b + c + d

    # Example 2: Using *args for variable number of arguments
    @staticmethod
    def add_args(*args):
        answer = 0
        for x in args:
            answer += x
        return answer

    # Example 3: Using **kwargs to accept named arguments
    @staticmethod
    def add_kwargs(**kwargs):
        answer = 0
        for value in kwargs.values():
            answer += value
        return answer


# ==========================
# Usage examples
# ==========================
if __name__ == "__main__":
    print("# Using default arguments")
    print(f"{MathOperations.add(1, 2)                       =   }")         # Output: 3
    print(f"{MathOperations.add(1, 2, 3)                    =   }")         # Output: 6
    print(f"{MathOperations.add(1, 2, 3, 4)                 =   }")         # Output: 10

    print("# Using *args")
    print(f"{MathOperations.add_args(1, 2)                  =   }")         # Output: 3
    print(f"{MathOperations.add_args(1, 2, 3)               =   }")         # Output: 6
    print(f"{MathOperations.add_args(1, 2, 3, 4)            =   }")         # Output: 10

    print("# Using **kwargs")
    print(f"{MathOperations.add_kwargs(a=1, b=2)            =   }")         # Output: 3
    print(f"{MathOperations.add_kwargs(a=1, b=2, c=3)       =   }")         # Output: 6
    print(f"{MathOperations.add_kwargs(a=1, b=2, c=3, d=4)  =   }")         # Output: 10
