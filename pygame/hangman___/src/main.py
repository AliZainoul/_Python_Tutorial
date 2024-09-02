import sys
from hangman import difficulty_levels, words_list
from ui.hangman_cli import HangmanCLI
from ui.hangman_pygame import HangmanPygame


def main_cli():
    difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
    if difficulty not in difficulty_levels:
        print("Invalid difficulty level. Defaulting to easy.")
        difficulty = "easy"
    game = HangmanCLI(words_list, difficulty)
    game.run()


def main_pygame():
    game = HangmanPygame()
    game.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "cli":
            main_cli()
        elif sys.argv[1] == "pygame":
            main_pygame()
    else:
        print("Invalid argument. Use 'cli' or 'pygame'.")
