class Cell:
    """
    Represents a single cell in the Minesweeper game grid.

    Attributes:
        _is_mine (bool): Indicates whether the cell contains a mine.
        _is_revealed (bool): Indicates whether the cell has been revealed.
        _is_flagged (bool): Indicates whether the cell is flagged as a possible mine by the player.
        _adjacent_mines (int): The number of mines adjacent to this cell.
    """
    
    def __init__(self):
        """
        Initializes a new Cell instance with default attributes.
        By default, the cell does not contain a mine, is not revealed, 
        is not flagged, and has zero adjacent mines.
        """
        self._is_mine = False
        self._is_revealed = False
        self._is_flagged = False
        self._adjacent_mines = 0

    @property
    def is_mine(self):
        """
        bool: Returns True if the cell contains a mine, False otherwise.
        """
        return self._is_mine

    @property
    def is_revealed(self):
        """
        bool: Returns True if the cell has been revealed, False otherwise.
        """
        return self._is_revealed

    @property
    def is_flagged(self):
        """
        bool: Returns True if the cell is flagged by the player as containing a mine, False otherwise.
        """
        return self._is_flagged

    @property
    def adjacent_mines(self):
        """
        int: Returns the number of mines adjacent to the cell.
        """
        return self._adjacent_mines

    def place_mine(self):
        """
        Places a mine in the cell by setting the _is_mine attribute to True.
        """
        self._is_mine = True

    def reveal(self):
        """
        Reveals the cell by setting the _is_revealed attribute to True, 
        unless the cell is flagged.
        """
        if not self._is_flagged:
            self._is_revealed = True

    def toggle_flag(self):
        """
        Toggles the flagged state of the cell. If the cell is not revealed, 
        the player can mark or unmark it as a potential mine.
        """
        if not self._is_revealed:
            self._is_flagged = not self._is_flagged
