"""
This script demonstrates the use of a while loop in Python.
It includes examples of basic while loops, using break and continue statements,
and a loop with a condition that depends on user input.
"""

def basic_while_loop():
    """Print numbers from 1 to 5 using a while loop."""
    print("Basic While Loop:")
    count = 1
    while count <= 5:
        print(count)
        count += 1

def while_with_break():
    """Demonstrate the use of a break statement in a while loop."""
    print("\nWhile Loop with Break:")
    count = 1
    while True:
        print(count)
        if count == 3:
            print("Breaking the loop.")
            break
        count += 1

def while_with_continue():
    """Demonstrate the use of a continue statement in a while loop."""
    print("\nWhile Loop with Continue:")
    count = 0
    while count < 5:
        count += 1
        if count == 3:
            print("Skipping number 3.")
            continue
        print(count)

def user_input_while_loop():
    """Keep asking the user for input until they type 'exit'."""
    print("\nUser Input While Loop:")
    while True:
        user_input = input("Type 'exit' to quit: ")
        if user_input.lower() == 'exit':
            print("Exiting the loop.")
            break
        print(f"You entered: {user_input}")

def main():
    """Main function to demonstrate various while loop examples."""
    basic_while_loop()
    while_with_break()
    while_with_continue()
    # Uncomment the line below to test the user input loop
    # user_input_while_loop()

if __name__ == "__main__":
    main()