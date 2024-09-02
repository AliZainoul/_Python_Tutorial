from hangman import Hangman


class HangmanCLI:
    def __init__(self, words: list[str], difficulty: str):
        self.hangman = Hangman(words, difficulty)

    def show_hangman(self):
        # Show the hangman in ASCII art
        hangman = [
            "  ____",
            " |    |",
            " |",
            " |",
            " |",
            " |",
            " |",
            " |",
            "_|_",
        ]
        if self.hangman.wrong_answers > 0:
            hangman[2] = " |    O"
        if self.hangman.wrong_answers > 1:
            hangman[3] = " |    |"
        if self.hangman.wrong_answers > 2:
            hangman[3] = " |   /|"
        if self.hangman.wrong_answers > 3:
            hangman[3] = " |   /|\\"
        if self.hangman.wrong_answers > 4:
            hangman[4] = " |   /"
        if self.hangman.wrong_answers > 5:
            hangman[4] = " |   / \\"

        print("\n".join(hangman))

    def run(self):
        # Play the game in the command line interface
        self.hangman.setup()
        print(
            "Difficulty:",
            self.hangman.difficulty,
            "Word length:",
            len(self.hangman.word),
            "Max tries:",
            self.hangman.max_tries,
        )
        while self.hangman.has_attempts_left():
            self.show_hangman()
            print(self.hangman.underlines)
            print(
                f"Tries left: {self.hangman.tries_left} Letters tried: {self.hangman.letters}"
            )
            letter = ""
            while True:
                letter = input("Enter a letter: ").upper()
                try:
                    message = self.hangman.play_letter(letter)
                    if message:
                        print(message)
                    break
                except ValueError:
                    print("Invalid input. Please enter a letter.")
        if self.hangman.has_won():
            print(f"Congratulations! You found the word: {self.hangman.word}")
        else:
            print(f"Game over! The word was: {self.hangman.word}")
