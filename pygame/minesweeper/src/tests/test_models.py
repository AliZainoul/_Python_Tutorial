import pytest
from minesweeper.models.cell import Cell
from minesweeper.models.board import MinesweeperBoard
from minesweeper.models.gamestate import GameState

@pytest.fixture
def sample_board():
    return MinesweeperBoard(5, 5, 3)

@pytest.fixture
def sample_game_state():
    return GameState(5, 5, 3)

def test_cell_initial_state():
    cell = Cell()
    assert not cell.is_mine
    assert not cell.is_revealed

def test_mine_placement(sample_board):
    mine_count = sum([1 for row in sample_board.grid for cell in row if cell.is_mine])
    assert mine_count == 3

def test_reveal_cell(sample_game_state):
    game_state = sample_game_state
    game_state.reveal(0, 0)
    assert game_state.board.grid[0][0].is_revealed

