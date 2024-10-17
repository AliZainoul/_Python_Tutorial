# METHOD OVERLOADING --> COMPILE TIME POLYMORPHISM

class MathOperations:
    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b
    
    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def add(a: str, b: str) -> str:
        return a + b
    
    @staticmethod
    def add(a: list, b: list) -> list:
        return a + b

    
print(MathOperations.add(2, 3))  # Output: 5
print(MathOperations.add(2.2, 3.3))  # Output: 5.5
print(MathOperations.add( "Hello ", str(input("Enter your name: "))))  # Output: Hello <Name>
print(MathOperations.add([1,2,3] , [4,5,6]))  # Output: Hello [1,2,3,4,5,6]

