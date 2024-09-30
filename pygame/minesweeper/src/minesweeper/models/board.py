import random
from minesweeper.models.cell import Cell

class MinesweeperBoard:
    """
    Represents the Minesweeper game board consisting of a grid of cells.

    Attributes:
        rows (int): The number of rows in the grid.
        cols (int): The number of columns in the grid.
        mines (int): The total number of mines to be placed on the board.
        grid (list): A 2D list representing the game board, where each element is a Cell instance.
        remaining_cells (int): The number of non-mine cells remaining to be revealed.
    """

    def __init__(self, rows, cols, mines):
        """
        Initializes the MinesweeperBoard with the given number of rows, columns, and mines.

        Args:
            rows (int): The number of rows for the grid.
            cols (int): The number of columns for the grid.
            mines (int): The total number of mines to be placed on the board.
        """
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.grid = [[Cell() for _ in range(cols)] for _ in range(rows)]
        self.remaining_cells = rows * cols - mines
        self._place_mines()
        self._calculate_adjacent_mines()

    def _place_mines(self):
        """
        Randomly places mines on the board by choosing random positions within the grid.
        The number of mines placed equals the `self.mines` attribute.
        """
        positions = random.sample(range(self.rows * self.cols), self.mines)
        for pos in positions:
            row, col = divmod(pos, self.cols)
            self.grid[row][col].place_mine()

    def _calculate_adjacent_mines(self):
        """
        Calculates and assigns the number of adjacent mines for each cell that is not a mine.
        For each non-mine cell, the adjacent mine count is stored in the `_adjacent_mines` attribute.
        """
        for row in range(self.rows):
            for col in range(self.cols):
                if not self.grid[row][col].is_mine:
                    self.grid[row][col]._adjacent_mines = self._count_adjacent_mines(row, col)

    def _count_adjacent_mines(self, row, col):
        """
        Counts the number of mines surrounding a given cell.

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.

        Returns:
            int: The number of mines surrounding the given cell.
        """
        count = 0
        for r in range(max(0, row-1), min(self.rows, row+2)):
            for c in range(max(0, col-1), min(self.cols, col+2)):
                if self.grid[r][c].is_mine:
                    count += 1
        return count

    def reveal_cell(self, row, col):
        """
        Reveals the cell at the specified position. If the cell contains a mine, the game is lost.

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.

        Raises:
            Exception: If a mine is revealed, indicating that the game is over.
        """
        if self.grid[row][col].is_mine:
            raise Exception('Game Over: Hit a mine!')
        self._flood_fill(row, col)

    def _flood_fill(self, row, col):
        """
        Recursively reveals cells on the board starting from the specified position. If the cell has no adjacent mines, 
        it continues to reveal neighboring cells that also have no adjacent mines, simulating the "flood fill" behavior 
        seen in Minesweeper.

        Args:
            row (int): The row index of the starting cell.
            col (int): The column index of the starting cell.

        Details:
            - If the current cell is already revealed, the recursion stops for that cell.
            - The cell is revealed using the `reveal()` method.
            - If the cell has no adjacent mines (`adjacent_mines == 0`), the method recursively reveals all neighboring cells.
            - The recursion is bounded by the grid's size, ensuring it only processes cells within valid grid boundaries.

        Explanation of max and min parameters:
            - In the nested loops, the parameters for `max(0, row-1)` and `min(self.rows, row+2)` (similarly for columns) are 
            carefully chosen to ensure that the flood fill process does not attempt to access cells outside the grid.
            - The `+2` in the `min` function ensures that the iteration includes the full range of neighbors in the 3x3 block 
            around the current cell, compensating for Python’s `range()` function's exclusive upper bound.
            
        **Developper Stories**:

        1. **As a Developper**, I expect the game to check all neighboring cells when I reveal a cell, including the diagonals (and anti diagonals).
            - The `+2` ensures that when revealing neighboring cells, the top-right, bottom-left, and other diagonals are included in the range.
            - Example: If the current cell is at `(2, 2)`, the algorithm checks all neighbors from `(1, 1)` to `(3, 3)`, forming a 3x3 block.

        2. **As a Developper**, I expect the game to handle cells near the top edge of the board without errors.
            - For cells in the first row (`row == 0`), `max(0, row-1)` ensures the loop doesn’t try to access negative rows, while `min(self.rows, row+2)` allows checking the valid row range, including the second row.
            - Example: If `row == 0`, the loop will check rows from `0` to `1` (since `row+1 == 1` and `row+2 == 2` compensates for Python's exclusive range).

        3. **As a Developper**, I expect the game to handle cells near the bottom edge of the board without errors.
            - The `+2` ensures that the algorithm includes the row directly below the current cell in the flood fill, but stops at the last valid row.
            - For cells near the bottom (`row == self.rows - 1`), `min(self.rows, row+2)` ensures that the loop stops at the last valid row.
            - Example: If `row == 4` on a 5x5 grid (`self.rows == 5`), `min(self.rows, row+2)` results in `min(5, 6)`, which is 5. So, the loop checks rows `3` and `4`, without exceeding the grid.

        4. **As a Developper**, I expect the game to handle cells near the left edge of the board without errors.
            - For cells in the first column (`col == 0`), `max(0, col-1)` ensures that the loop doesn’t try to access negative columns, while `min(self.cols, col+2)` allows checking valid columns.
            - Example: If `col == 0`, the loop checks columns from `0` to `1`.

        5. **As a Developper**, I expect the game to handle cells near the right edge of the board without errors.
            - The `+2` ensures that the algorithm includes the column directly to the right of the current cell in the flood fill, but stops at the last valid column.
            - For cells near the right edge (`col == self.cols - 1`), `min(self.cols, col+2)` ensures that the loop stops at the last valid column.
            - Example: If `col == 4` on a 5x5 grid (`self.cols == 5`), `min(self.cols, col+2)` results in `min(5, 6)`, which is 5. So, the loop checks columns `3` and `4`.

        6. **As a Developper**, I expect the game to recursively reveal all neighboring cells that have no adjacent mines, regardless of their location on the board.
            - By using `max(0, row-1)` and `min(self.rows, row+2)`, the algorithm dynamically adjusts the range to include all valid neighboring cells, whether the cell is in the middle or near the edges of the board.
            - Example: For a cell in the middle of a 5x5 grid (e.g., `(2, 2)`), the range for rows would be from `1` to `3`, and the range for columns would be from `1` to `3`, checking all neighboring cells.

        Example Behavior:
            - If the user reveals a cell with no adjacent mines in the top-left corner of the grid (0, 0), the `flood_fill` method will correctly start from this cell 
            and attempt to reveal neighboring cells (0, 0), (0, 1), (1, 0), and (1, 1), without trying to access cells with negative indices.
            - The method ensures that the recursion respects the board boundaries by using the `max` and `min` functions to restrict row and column indices to valid ranges.
        """
        if self.grid[row][col].is_revealed:
            # Base case: Stop if the cell is already revealed
            return

        # Reveal the current cell
        self.grid[row][col].reveal()

        # If no adjacent mines, recursively reveal neighboring cells
        if self.grid[row][col].adjacent_mines == 0:
            for r in range(max(0, row-1), min(self.rows, row+2)):
                for c in range(max(0, col-1), min(self.cols, col+2)):
                    self._flood_fill(r, c)
