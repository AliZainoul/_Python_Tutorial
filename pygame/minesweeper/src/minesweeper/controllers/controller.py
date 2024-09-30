class GameController:
    """
    Manages the game logic and interacts with the view and game state.

    Attributes:
        game_state (GameState): The current state of the game.
        view (object): The view responsible for displaying the game state to the user.
    """

    def __init__(self, game_state, view):
        """
        Initializes the GameController with the given game state and view.

        Args:
            game_state (GameState): The game state to manage.
            view (object): The view to use for displaying game information.
        """
        self.game_state = game_state
        self.view = view

    def process_input(self, user_input):
        """
        Processes user input to perform actions in the game. 

        The input should be in the format 'command row col', where 'command' is 'r' for reveal or 'f' for flag,
        'row' is the row index, and 'col' is the column index. Updates the game state and view based on the input.

        Args:
            user_input (str): The input string from the user.
        """
        try:
            command, row, col = user_input.split()
            row, col = int(row), int(col)
        except ValueError:
            self.view.display_message('Invalid input. Format: [r|f] row col')
            return

        match command:
            case 'r':
                self.game_state.reveal(row, col)
            case 'f':
                self.game_state.toggle_flag(row, col)
            case _:
                self.view.display_message('Invalid command.')

    def run(self):
        """
        Starts the game loop, continuously updating the view and processing user input until the game ends or is won.
        """
        while self.game_state.game_status == 'active':
            self.view.display_board(self.game_state.board)
            user_input = input('Enter command (r/f row col): ')
            self.process_input(user_input)
        
        # Display final game state message
        match self.game_state.game_status:
            case 'game_over':
                self.view.display_message('Game Over!')
            case 'victory':
                self.view.display_message('You Win!')
