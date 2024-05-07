class MathOperations:
    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b
    
    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

print(MathOperations.add(2, 3))  # Output: 5
print(MathOperations.add(2.2, 3.3))  # Output: 5.5
