import pygame
from ui.gui import GUI
from hangman import Hangman

class HangmanController:
    """
    Manages the game logic for the Hangman game, including user input, updating
    the view, and controlling the game flow. Interfaces with the model and view
    components to handle game state and user interactions.
    """

    def __init__(self, model, view):
        """
        Initializes the HangmanController with the specified model and view.

        Args:
            model (Hangman): The game model that manages the game state and logic.
            view (GUI): The view that handles displaying the game state and user interface.
        
        Pygame Documentation:
        - `pygame.event.get()`: https://www.pygame.org/docs/ref/event.html#pygame.event.get
        """
        self.model = model
        self.view = view
        self.game_started = False
        self.game_over = False

    def process_input(self, event):
        """
        Processes user input events, including quitting the game, starting a new game,
        and processing letter guesses if the game is ongoing.

        Args:
            event (pygame.event.Event): The event object representing the user input.

        Returns:
            bool: True if the game should continue running, False if the user wants to quit.

        Pygame Documentation:
        - `pygame.QUIT`: https://www.pygame.org/docs/ref/event.html#pygame.QUIT
        - `pygame.MOUSEBUTTONDOWN`: https://www.pygame.org/docs/ref/event.html#pygame.MOUSEBUTTONDOWN
        - `pygame.KEYDOWN`: https://www.pygame.org/docs/ref/event.html#pygame.KEYDOWN
        """
        if event.type == pygame.QUIT:
            return False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked_button = self.view.check_button_click(event.pos)
            if clicked_button == 'start':
                self.start_game()
            elif clicked_button == 'quit':
                return False
        
        if event.type == pygame.KEYDOWN and self.game_started and not self.game_over:
            if event.unicode.isalpha():
                self.model.guess_letter(event.unicode.lower())
                self.update_view()  # Update the view after guessing a letter
                if self.model.is_game_over():
                    self.end_game()

        return True

    def update_view(self):
        """
        Updates the view based on the current game state. If the game is over,
        it displays the final state and a prompt to play again or quit.

        Pygame Documentation:
        - `pygame.display.flip()`: https://www.pygame.org/docs/ref/display.html#pygame.display.flip
        """
        current_state = self.model.get_display_word()
        attempts_left = self.model.attempts_left
        game_over_message = ""

        if self.game_over:
            if "_" not in self.model.get_display_word():
                game_over_message = "You Win!"
            else:
                game_over_message = f"Game Over! The word was '{self.model.word_to_guess.upper()}'"
        
        self.view.draw_screen(current_state, attempts_left, game_over_message)

        if self.game_over:
            self.view.display_message(
                "Press 'Start Game' to play again or 'Quit' to exit.",
                (self.view.screen.get_width() // 2, self.view.screen.get_height() // 2 + 200)
            )

        pygame.display.flip()

    def run_game_loop(self):
        """
        Main game loop that processes input and updates the view. Runs until the user quits the game.

        Pygame Documentation:
        - `pygame.display.update()`: https://www.pygame.org/docs/ref/display.html#pygame.display.update
        - `pygame.quit()`: https://www.pygame.org/docs/ref/quit.html#pygame.quit
        """
        running = True
        while running:
            for event in pygame.event.get():
                running = self.process_input(event)
            pygame.display.update()
        pygame.quit()

    def start_game(self):
        """
        Initializes a new game by resetting the model and updating the view. 
        This method starts a new game and prepares the game state for user interaction.

        Pygame Documentation:
        - `pygame.font.SysFont()`: https://www.pygame.org/docs/ref/font.html#pygame.font.SysFont
        """
        self.model.reset_game(['python', 'hangman', 'example'])
        self.game_started = True
        self.game_over = False
        self.update_view()  # Initialize the game view with underscores

    def end_game(self):
        """
        Ends the current game and displays the final state. Stops further input until a new game is started.
        
        Pygame Documentation:
        - `pygame.display.flip()`: https://www.pygame.org/docs/ref/display.html#pygame.display.flip
        """
        self.game_over = True
        self.update_view()  # Display the final game state and message
