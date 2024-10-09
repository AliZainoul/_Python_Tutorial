import random

def choose_random_word(words: list) -> str:
    """Choose a random word from the provided list."""
    return random.choice(words)

def display_word_state(word: str, correct_guesses: set) -> str:
    """Return the current state of the word with unguessed letters as underscores."""
    return ' '.join([letter if letter in correct_guesses else '_' for letter in word])
    '''
    # Equivalent to:
    list_of_correct_guesses = []

    for letter in word:
        if letter in correct_guesses:
            list_of_correct_guesses.append(letter)
        else:
            list_of_correct_guesses.append("_")

    return ' '.join(list_of_correct_guesses)
    '''


def hangman():
    """Main function to play the Hangman game."""
    words = ['hangman']
    word = choose_random_word(words)
    attempts_remaining = 6
    correct_guesses = set()
    all_guesses = set()

    print("Welcome to Hangman!")
    
    while attempts_remaining > 0:
        print(f"\nWord: {display_word_state(word, correct_guesses)}")
        print(f"Attempts remaining: {attempts_remaining}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please guess a single letter.")
            continue

        if guess in all_guesses:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue
        
        all_guesses.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            correct_guesses.add(guess)
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            attempts_remaining -= 1

        if all(letter in correct_guesses for letter in word):
            print(f"\nCongratulations! You've guessed the word: {word}")
            break
    else:
        print(f"\nGame over! The word was: {word}")

if __name__ == "__main__":
    hangman()