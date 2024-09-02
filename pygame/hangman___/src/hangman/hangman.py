import random

difficulty_levels = {
    "easy": {"number_of_tries": 6, "word_length": 6},
    "medium": {"number_of_tries": 4, "word_length": 8},
    "hard": {"number_of_tries": 3, "word_length": 10},
}

words_list = [
    "CPP",
    "CSS",
    "PHP",
    "SQL",
    "HTML",
    "JAVA",
    "PERL",
    "RUBY",
    "RUST",
    "SCALA",
    "SWIFT",
    "GOLANG",
    "KOTLIN",
    "PYTHON",
    "JAVASCRIPT",
]


class Hangman:
    def __init__(self, words: list[str], difficulty: str):
        self.difficulty = difficulty
        self.words = words

    @property
    def tries_left(self):
        # Calculate the number of tries
        return self.max_tries - self.wrong_answers

    def choose_word(self) -> str:
        # Choose a random word from the list of words
        return random.choice(
            [word for word in self.words if len(word) >= self.min_chars]
        )

    def show_underlines(self) -> str:
        # Show underlines for each letter in the word
        return "_ " * len(self.word)

    def is_letter_in_word(self, letter: str) -> bool:
        # Check if the letter is in the word
        return letter in self.word

    def show_letter(self, letter: str):
        # Show the letter in the underlines
        if self.is_letter_in_word(letter):
            new_underlines = ""
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    new_underlines += letter + " "
                else:
                    new_underlines += self.underlines[i * 2] + " "
            self.underlines = new_underlines

    def is_letter(self, letter: str) -> bool:
        # Check if the input is a letter
        return letter.isalpha() and len(letter) == 1

    def play_letter(self, letter: str) -> str:
        if not self.is_letter(letter):
            raise ValueError("Invalid input. Please enter a letter.")

        # Play a letter and return a message
        if letter in self.letters:
            return "You already tried this letter."

        self.letters.append(letter)
        if self.is_letter_in_word(letter):
            self.show_letter(letter)
        else:
            self.wrong_answers += 1
            return "Wrong letter!"

    def has_won(self) -> bool:
        # Check if the player has won
        return self.underlines.count("_") == 0

    def has_attempts_left(self) -> bool:
        # Check if the player has attempts left
        return self.wrong_answers < self.max_tries and self.underlines.count("_") > 0

    def setup(self, word: str = None):
        # Setup the game
        self.min_chars = difficulty_levels[self.difficulty]["word_length"]
        self.max_tries = difficulty_levels[self.difficulty]["number_of_tries"]
        self.word = word if word is not None else self.choose_word()
        self.underlines = self.show_underlines()
        self.wrong_answers = 0
        self.letters = []
