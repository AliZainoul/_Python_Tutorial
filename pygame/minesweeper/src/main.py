from minesweeper.models.gamestate import GameState
from minesweeper.views.terminal_view import TerminalView
from minesweeper.controllers.controller import GameController

def main():
    # Set up the game parameters
    rows, cols, mines = 9, 9, 10  # Beginner mode settings

    # Initialize the game state (model)
    game_state = GameState(rows, cols, mines)

    # Initialize the view
    view = TerminalView()

    # Initialize the controller with the game state and view
    controller = GameController(game_state, view)

    # Start the game loop
    print("Welcome to Terminal Minesweeper!")
    print("Commands: 'r row col' to reveal, 'f row col' to flag/unflag.")
    print(f"Starting game: {rows}x{cols} grid with {mines} mines.\n")

    controller.run()

if __name__ == "__main__":
    main()
