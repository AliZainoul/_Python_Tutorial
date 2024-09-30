from minesweeper.models.board import MinesweeperBoard

class GameState:
    """
    Represents the state of the Minesweeper game.

    Attributes:
        board (MinesweeperBoard): The game board containing cells and mines.
        game_status (str): The current status of the game. Can be 'active', 'game_over', or 'victory'.
    """

    def __init__(self, rows, cols, mines):
        """
        Initializes the GameState with a new Minesweeper board and sets the initial game status.

        Args:
            rows (int): The number of rows in the game board.
            cols (int): The number of columns in the game board.
            mines (int): The number of mines to be placed on the board.
        """
        self.board = MinesweeperBoard(rows, cols, mines)
        self.game_status = 'active'  # Possible values: 'active', 'game_over', 'victory'

    def reveal(self, row, col):
        """
        Reveals the cell at the specified position. If the cell contains a mine, the game status is set to 'game_over'.

        Args:
            row (int): The row index of the cell to reveal.
            col (int): The column index of the cell to reveal.
        """
        try:
            self.board.reveal_cell(row, col)
            if self.check_victory():
                self.game_status = 'victory'
        except Exception:
            self.game_status = 'game_over'

    def toggle_flag(self, row, col):
        """
        Toggles the flag status of the cell at the specified position.

        Args:
            row (int): The row index of the cell to toggle.
            col (int): The column index of the cell to toggle.
        """
        self.board.grid[row][col].toggle_flag()

    def check_victory(self):
        """
        Checks if the game has been won by revealing all non-mine cells.

        Returns:
            bool: True if the game is won, False otherwise.
        """
        return all(cell.is_revealed or cell.is_mine for row in self.board.grid for cell in row)
