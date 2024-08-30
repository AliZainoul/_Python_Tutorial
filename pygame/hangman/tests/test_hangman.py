import pytest
from src.hangman.hangman import Hangman


@pytest.fixture
def hangman():
    """
    Fixture to create a Hangman instance for use in tests.
    """
    return Hangman(['python', 'hangman', 'example'])

def test_initialization(hangman):
    """
    Test the initial state of the Hangman game.
    """
    assert hangman.word_list == ['python', 'hangman', 'example']
    assert hangman.word_to_guess == ""
    assert hangman.guessed_letters == []
    assert hangman.correct_guesses == []
    assert hangman.max_attempts == 6
    assert hangman.attempts_left == 6

def test_reset_game(hangman):
    """
    Test the reset_game method to ensure it correctly initializes a new game.
    """
    hangman.reset_game(['test', 'word'])
    assert hangman.word_to_guess in ['test', 'word']
    assert hangman.guessed_letters == []
    assert hangman.correct_guesses == ["_" for _ in hangman.word_to_guess]
    assert hangman.attempts_left == 6

def test_guess_correct_letter(hangman):
    """
    Test guessing a correct letter.
    """
    hangman.reset_game(['python'])
    hangman.guess_letter('p')
    assert 'p' in hangman.guessed_letters
    assert hangman.correct_guesses == ['p', '_', '_', '_', '_', '_']
    assert hangman.attempts_left == 6

def test_guess_incorrect_letter(hangman):
    """
    Test guessing an incorrect letter.
    """
    hangman.reset_game(['python'])
    hangman.guess_letter('z')
    assert 'z' in hangman.guessed_letters
    assert hangman.correct_guesses == ['_', '_', '_', '_', '_', '_']
    assert hangman.attempts_left == 5

def test_get_display_word(hangman):
    """
    Test the get_display_word method.
    """
    hangman.reset_game(['hangman'])
    hangman.guess_letter('h')
    hangman.guess_letter('a')
    assert hangman.get_display_word() == "h a _ _ _ a _"

def test_is_game_over_win(hangman):
    """
    Test the is_game_over method when the player has won.
    """
    hangman.reset_game(['python'])
    for letter in 'python':
        hangman.guess_letter(letter)
    assert hangman.is_game_over() is True

def test_is_game_over_loss(hangman):
    """
    Test the is_game_over method when the player has lost.
    """
    hangman.reset_game(['python'])
    hangman.guess_letter('z')  # Guessing wrong letters
    hangman.guess_letter('x')
    hangman.guess_letter('y')
    hangman.guess_letter('w')
    hangman.guess_letter('v')
    hangman.guess_letter('u')
    hangman.guess_letter('m')
    assert hangman.is_game_over() is True

def test_is_game_over_not_over(hangman):
    """
    Test the is_game_over method when the game is not yet over.
    """
    hangman.reset_game(['python'])
    hangman.guess_letter('p')
    assert hangman.is_game_over() is False
