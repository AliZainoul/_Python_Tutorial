import random

RANDOM_NUMBER = random.randint(1, 100)
UP, DOWN = ("up", "down")
attempts = 0

def guess_number(input_number):
    global attempts
    if input_number == RANDOM_NUMBER:
        print("Found, in " ,attempts+1, "attempts. \n")
        return
    attempts += 1
    guess_number(
        int(input(
            f"Please {DOWN if input_number > RANDOM_NUMBER else UP}grade, please enter a new number: \n")))
    
guess_number(int(input("Please enter your number: \n")))



"""
import random

def guessing_game():
    '''
        Play a game where the user guesses a number between 1 and 100.
    '''
    target_number = random.randint(1, 100)
    attempts = 0
    print("I have selected a number between 1 and 100. Try to guess it!")

    while True:
        guess = input("Enter your guess: ")
        try:
            guess = int(guess)
            attempts += 1
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if guess < target_number:
            print("Higher!")
        elif guess > target_number:
            print("Lower!")
        else:
            print(f"Congratulations! You've guessed the correct number in {attempts} attempts.")
            break

def main():
    guessing_game()

if __name__ == "__main__":
    main()
"""