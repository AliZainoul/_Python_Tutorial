import pytest

@pytest.fixture
def game_state():
    from minesweeper.models.gamestate import GameState
    return GameState(5, 5, 3)

