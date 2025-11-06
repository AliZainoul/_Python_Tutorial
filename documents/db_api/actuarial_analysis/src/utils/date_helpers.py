"""Date utility functions."""

import random
from datetime import date
from typing import Optional


def generate_random_birth_date(min_age: int, max_age: int, ref_date: date = None) -> date:
    """
    Generate a random birth date that results in an age between min_age and max_age.

    Args:
        min_age: minimum age
        max_age: maximum age
        ref_date: reference date (default: today)

    Returns:
        date object representing birth_date
    """
    if ref_date is None:
        ref_date = date.today()
    
    age = random.randint(min_age, max_age)
    birth_year = ref_date.year - age
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    
    return date(birth_year, month, day)


def calculate_age(birth_date: Optional[date], ref_date: date) -> Optional[int]:
    """
    Calculate age at a reference date.
    
    Args:
        birth_date: date of birth
        ref_date: reference date
    
    Returns:
        age in years, or None if birth_date is None
    """
    if birth_date is None:
        return None
    
    return ref_date.year - birth_date.year - (
        (ref_date.month, ref_date.day) < (birth_date.month, birth_date.day)
    )


def get_age_bucket(age: Optional[int]) -> str:
    """
    Classify age into a bucket.
    
    Args:
        age: age in years (None for unknown)
    
    Returns:
        bucket label ('0-25', '26-45', '46-65', '66+', 'unknown')
    """
    if age is None:
        return "unknown"
    elif age <= 25:
        return "0-25"
    elif age <= 45:
        return "26-45"
    elif age <= 65:
        return "46-65"
    else:
        return "66+"


def create_safe_date(year: int, month: int, day: int) -> date:
    """
    Create a date, ensuring day is valid for the month.
    
    Args:
        year: year
        month: month
        day: day (will be capped at 28 to avoid invalid dates)
    
    Returns:
        date object
    """
    safe_day = min(day, 28)
    return date(year, month, safe_day)