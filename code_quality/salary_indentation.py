"""
This script calculates the total salary by adding base salary and bonus.
It raises a ValueError if either base salary or bonus is negative.
"""

def calculate_salary(base: float, bonus: float) -> float: 
    """ an INDENTED little function in order to calculate salary"""
    total : float = float(base + bonus)
    
    if base < 0 or bonus < 0:
        raise ValueError("Base salary and bonus must be non-negative")
    
    return total


def main() -> None:
    try :
        sum_salary : float = calculate_salary(50000.0044, 5000.46)
        print(sum_salary)
    except IndentationError:
        raise IndentationError("Incorrect indentation in the function definition")
    finally:
        print("Salary calculated successfully")

if __name__ == "__main__":
    main()

# The main function calls calculate_salary and handles any exceptions.
