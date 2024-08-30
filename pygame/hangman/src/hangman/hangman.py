import random

class Hangman:
    """
    A class to represent the Hangman game.

    Attributes:
    ----------
    word_list : list
        A list of words from which the game will choose the word to guess.
    word_to_guess : str
        The word that the player needs to guess.
    guessed_letters : list
        A list of letters that the player has guessed so far.
    correct_guesses : list
        A list that represents the current state of the guessed word with underscores for unguessed letters.
    max_attempts : int
        The maximum number of incorrect guesses allowed.
    attempts_left : int
        The number of incorrect guesses remaining.

    Methods:
    -------
    reset_game(word_list=None):
        Resets the game state, choosing a new word from the word list.
    guess_letter(letter):
        Processes a player's guess, updating the game state accordingly.
    get_display_word():
        Returns the current state of the word being guessed, with underscores for unguessed letters.
    is_game_over():
        Checks whether the game has ended, either by guessing the word or by running out of attempts.
    """

    def __init__(self, word_list):
        """
        Initialize the Hangman game with a list of words.

        Parameters:
        ----------
        word_list : list
            A list of words to be used in the game.
        """
        self.word_list = word_list
        self.word_to_guess = ""
        self.guessed_letters = []
        self.correct_guesses = []
        self.max_attempts = 6
        self.attempts_left = self.max_attempts

    def reset_game(self, word_list=None):
        """
        Resets the game state, choosing a new word from the word list.

        Parameters:
        ----------
        word_list : list, optional
            A new list of words to choose from (default is None, which uses the existing word_list).

        This method resets the guessed letters, correct guesses, and attempts left.
        """
        if word_list:
            self.word_list = word_list
        self.word_to_guess = random.choice(self.word_list).lower()
        self.guessed_letters = []
        self.correct_guesses = ["_" for _ in self.word_to_guess]
        self.attempts_left = self.max_attempts

    def guess_letter(self, letter):
        """
        Processes a player's guess, updating the game state accordingly.

        Parameters:
        ----------
        letter : str
            The letter guessed by the player.

        This method checks if the letter is in the word to guess and updates the correct guesses or reduces the attempts left.
        """
        if letter in self.guessed_letters:
            return
        self.guessed_letters.append(letter)
        if letter in self.word_to_guess:
            for idx, char in enumerate(self.word_to_guess):
                if char == letter:
                    self.correct_guesses[idx] = letter
        else:
            self.attempts_left -= 1

    def get_display_word(self):
        """
        Returns the current state of the word being guessed, with underscores for unguessed letters.

        Returns:
        -------
        str
            The word with guessed letters revealed and unguessed letters as underscores.
        """
        return " ".join(self.correct_guesses)

    def is_game_over(self):
        """
        Checks whether the game has ended based on win or loss conditions.

        Returns:
        -------
        bool
            True if the game has ended (either by guessing the word or running out of attempts), otherwise False.
        """
        # Game is over if the word is completely guessed or attempts are exhausted
        return "_" not in self.correct_guesses or self.attempts_left <= 0
