# Example of static methods
class Calculator:
    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b
    @staticmethod
    def sub(a: float, b: float) -> float:
        return a - b
    @staticmethod
    def prod(a: float, b: float) -> float:
        return a * b
    @staticmethod
    def divi(a: float, b: float) -> float:
        try: 
            result : float =  a / b
            return result
        except ZeroDivisionError as e:
            print(e)
            return -1

def main():
    print(f"{Calculator.add(1.4, 2.1)   = }")
    print(f"{Calculator.sub(1.4, 2.1)   = }")
    print(f"{Calculator.prod(1.4, 2.1)  = }")
    print(f"{Calculator.divi(1.4, 2.1)  = }")
    print(f"{Calculator.divi(1.4, 0)    = }")


if __name__ == "__main__":
    main()
