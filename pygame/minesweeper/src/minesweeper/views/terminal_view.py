class TerminalView:
    def display_board(self, board):
        for row in board.grid:
            print(' '.join(['F' if cell.is_flagged else '*' if not cell.is_revealed else str(cell.adjacent_mines) for cell in row]))

    def display_message(self, message):
        print(message)

