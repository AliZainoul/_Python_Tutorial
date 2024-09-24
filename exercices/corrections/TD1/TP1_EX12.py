'''
import random

def roll_die() -> int:
    """Simulate rolling a single die and return the result."""
    die = random.randint(1, 6)
    return die

def roll_dice() -> int:
    """Simulate rolling two dice and return the sum."""
    die1 = roll_die()
    die2 = roll_die()
    return die1 + die2

def simulate_dice_rolls(rolls: int):
    """Simulate a certain number of die rolls and count the frequency of each sum."""
    results = {i: 0 for i in range(2, 13)}  # Initialize counts for sums 2 through 12
    
    for _ in range(rolls):
        dice_sum = roll_dice()
        results[dice_sum] += 1

    print(f"\nResults after {rolls} rolls:")
    for result, count in results.items():
        print(f"Sum {result}: {count} times")

def main():
    print("Dice Roll Simulation")
    rolls = int(input("Enter the number of rolls: "))
    simulate_dice_rolls(rolls)

if __name__ == "__main__":
    main()



'''
import random
from collections import Counter

def simulate_dice_rolls(rolls: int):
    """
    Simulate rolling two dice a specified number of times and count the frequency of each possible sum.

    Args:
        rolls (int): The number of times to roll two dice.

    Returns:
        None: The function prints the frequency of each possible dice sum (from 2 to 12) after all rolls.

    Process:
        - Rolls two dice using random.randint(1, 6) for the specified number of rolls.
        - Stores the sum of each roll in a list.
        - Uses the Counter class from collections to count how many times each sum (from 2 to 12) occurs.
        - Prints the result for each sum, including sums that appear 0 times.

    Notes:
        The Counter is used to efficiently count occurrences of each dice sum. The result_counts.get(result, 0)
        method is used to handle cases where a particular dice sum might not be present in the Counter (i.e., when it occurs 0 times).

    Example:
        If 100 rolls are simulated, the function might output:
        Sum 2: 3 times
        Sum 3: 7 times
        ...
        Sum 12: 8 times
    """
    # Roll two dice and store the sums using list comprehension
    sums = [random.randint(1, 6) + random.randint(1, 6) for _ in range(rolls)]
    
    # Use Counter to count the occurrences of each sum
    result_counts = Counter(sums)
    
    print(f"\nResults after {rolls} rolls:")
    for result in range(2, 13):
        # result_counts.get(result, 0) ensures that if a sum does not occur, it returns 0 instead of raising a KeyError
        print(f"Sum {result}: {result_counts.get(result, 0)} times")

def main():
    """
    Main function to drive the dice roll simulation.

    Asks the user to input the number of rolls and then calls simulate_dice_rolls()
    to simulate the dice rolls and display the results.
    """
    print("Dice Roll Simulation")
    rolls = int(input("Enter the number of rolls: "))
    simulate_dice_rolls(rolls)

if __name__ == "__main__":
    main()


'''
# Efficiency Comparison (Ignoring numpy):
# 
# 1. Dictionary-Based Solution: O(rolls) 
#    - Most efficient in practice.
#
# 2. Counter Solution: O(rolls)
#    - Efficient and more elegant for handling counts automatically.
#
# 3. .count() Solution: O(rolls * 11)
#    - Least efficient due to multiple linear scans.
#
# Conclusion:
# - Most Efficient: The dictionary-based solution (manual or using Counter) is the most efficient
#   for large numbers of rolls.
# - Best Choice: The Counter solution is both efficient and cleaner for readability. However, for 
#   extremely large datasets, the manual dictionary method might slightly outperform Counter by 
#   avoiding a secondary pass over the data.
# - Final Verdict: The dictionary-based approach (manual or with Counter) is optimal, while the 
#   .count() method is the least efficient of the three.

'''