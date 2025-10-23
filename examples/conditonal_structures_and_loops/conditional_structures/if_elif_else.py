"""
This script demonstrates the use of if, elif, and else statements in Python.
It includes multiple examples to illustrate conditional structures and best practices.
"""

# Example 0: Basic if statement
def is_positive(number: float) -> str:
    """
    Checks if a number is positive.
    
    Args:
        number (int or float): The number to check.

    Returns:
        str: A message indicating if the number is positive or not.
    """
    if number >= 0:
        return "The number is positive or equals to zero."
    else:
        return "The number is negative."

# Example 1: Basic if-else structure
def is_even(number: int) -> str:
    """
    Checks if a number is even or odd.
    
    Args:
        number (int): The number to check.

    Returns:
        str: A message indicating if the number is even or odd.
    """
    if number % 2 == 0:
        return "The number is even."
    else:
        return "The number is odd."

# Example 2: Basic if-elif-else structure
def check_number_sign(number : float) -> str:
    """
    Determines if a number is positive, negative, or zero.
    
    Args:
        number (int or float): The number to check.
    
    Returns:
        str: A message indicating the sign of the number.
    """
    if number > 0:
        return "The number is positive."
    elif number < 0:
        return "The number is negative."
    else:
        return "The number is zero."

# Example 3: Nested if-else
def categorize_age(age : int) -> str:
    """
    Categorizes a person based on their age.
    
    Args:
        age (int): The age of the person.
    
    Returns:
        str: A category based on the age.
    """
    if age < 0:
        return "Invalid age."
    elif age < 13:
        return "Child."
    elif age < 20:
        return "Teenager."
    elif age < 65:
        return "Adult."
    else:
        return "Senior."

# Example 4: Using if-elif-else with multiple conditions
def grade_student(score: int) -> str:
    """
    Assigns a grade based on a student's score.
    
    Args:
        score (int): The student's score (0-100).
    
    Returns:
        str: The grade corresponding to the score.
    """
    if score < 0 or score > 100:
        return "Invalid score."
    elif score >= 90:
        return "Grade: A"
    elif score >= 80:
        return "Grade: B"
    elif score >= 70:
        return "Grade: C"
    elif score >= 60:
        return "Grade: D"
    else:
        return "Grade: F"

# Example 5: Combining conditions with logical operators
def is_eligible_to_vote(age: int, citizenship : str) -> str:
    """
    Checks if a person is eligible to vote.
    
    Args:
        age (int): The age of the person.
        citizenship (str): The citizenship status of the person.
    
    Returns:
        str: A message indicating voting eligibility.
    """
    if age >= 18 and citizenship.lower() == "yes":
        return "You are eligible to vote."
    elif age < 18:
        return "You are not eligible to vote due to age."
    else:
        return "You are not eligible to vote due to citizenship."

# Example 6: Using if-elif-else with strings
def check_day_type(day):
    """
    Determines if a day is a weekday or weekend.
    
    Args:
        day (str): The name of the day.
    
    Returns:
        str: A message indicating the type of day.
    """
    day = day.lower()
    if day in ["saturday", "sunday"]:
        return "It's a weekend."
    elif day in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
        return "It's a weekday."
    else:
        return "Invalid day."


def main() -> None:
    print(is_positive(10))
    print(is_even(7))
    print(check_number_sign(-5))
    print(categorize_age(25))
    print(grade_student(85))
    print(is_eligible_to_vote(20, "yes"))
    print(check_day_type("Saturday"))


# Example usage
if __name__ == "__main__":
    main()
