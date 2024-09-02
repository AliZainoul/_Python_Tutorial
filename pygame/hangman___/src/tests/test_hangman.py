from pytest import fixture
import pytest
from hangman import Hangman


words_list = ["python", "java", "kotlin", "javascript"]
difficulty = "easy"


@fixture
def hangman():
    hangman = Hangman(words_list, difficulty)
    hangman.setup("python")
    return hangman


def test_is_letter(hangman):
    assert hangman.is_letter("a")
    assert not hangman.is_letter("1")
    assert not hangman.is_letter("ab")


def test_tries_left(hangman):
    hangman.max_tries = 5
    hangman.wrong_answers = 2
    assert hangman.tries_left == 3
    hangman.wrong_answers = 5
    assert hangman.tries_left == 0


def test_has_attempts_left(hangman):
    hangman.max_tries = 5
    hangman.wrong_answers = 2
    hangman.underlines = "______"
    assert hangman.has_attempts_left()
    hangman.wrong_answers = 5
    assert not hangman.has_attempts_left()
    hangman.wrong_answers = 2
    hangman.underlines = "python"
    assert not hangman.has_attempts_left()


def test_setup(hangman):
    assert hangman.min_chars == 6
    assert hangman.max_tries == 6
    assert hangman.word in words_list
    assert hangman.wrong_answers == 0
    assert hangman.letters == []


def test_choose_word(hangman):
    hangman.choose_word
    assert hangman.word in words_list


def test_is_letter_in_word(hangman):
    assert hangman.is_letter_in_word("p")
    assert not hangman.is_letter_in_word("z")


def test_show_letter(hangman):
    hangman.show_letter("p")
    assert hangman.underlines == "p _ _ _ _ _ "
    hangman.show_letter("z")
    assert hangman.underlines == "p _ _ _ _ _ "


def test_play_letter(hangman):
    hangman.play_letter("p")
    assert hangman.underlines == "p _ _ _ _ _ " and hangman.wrong_answers == 0


def test_play_letter_exception(hangman):
    with pytest.raises(ValueError):
        hangman.play_letter("1")
