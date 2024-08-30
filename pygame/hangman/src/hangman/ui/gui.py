import pygame

class GUI:
    """
    The GUI class handles the graphical user interface of the Hangman game.
    It manages the display of messages, the game state, and buttons for user interaction.

    Attributes:
    ----------
    screen : pygame.Surface
        The surface on which all the graphical elements are drawn.
    font : pygame.font.Font
        The font used for rendering text in the game.
    buttons : dict
        A dictionary mapping button names to their respective pygame.Rect objects.
    background_color : tuple
        RGB tuple representing the background color of the screen.
    button_color : tuple
        RGB tuple representing the color of the buttons.
    text_color : tuple
        RGB tuple representing the color of the text.
    """

    def __init__(self, screen, font):
        """
        Initializes the GUI with a screen, font, and default colors.

        Parameters:
        ----------
        screen : pygame.Surface
            The surface on which all the graphical elements are drawn.
        font : pygame.font.Font
            The font used for rendering text in the game.
        """
        self.screen = screen
        self.font = font
        self.buttons = {}
        self.background_color = (255, 255, 255)  # White background
        self.button_color = (100, 149, 237)  # Cornflower Blue
        self.text_color = (0, 0, 0)  # Black text
        self.initialize_display()

    def initialize_display(self):
        """
        Sets up the initial welcome screen with a message and buttons.

        This method clears the screen, displays a welcome message, and
        draws the Start and Quit buttons.

        Pygame Documentation:
        ---------------------
        - pygame.Surface.fill(): Fill the surface with a solid color.
          Reference: https://www.pygame.org/docs/ref/surface.html#pygame.Surface.fill
        
        - pygame.display.flip(): Update the full display Surface to the screen.
          Reference: https://www.pygame.org/docs/ref/display.html#pygame.display.flip
        """
        self.screen.fill(self.background_color)
        self.display_message("Welcome to Hangman", (self.screen.get_width() // 2, self.screen.get_height() // 4))
        self.draw_buttons()
        pygame.display.flip()

    def draw_screen(self, word: str, attempts_left: int, game_over_message: str):
        """
        Draws the current game state, including the word with underscores, the number of attempts left, and any game over message.

        Parameters:
        ----------
        word : str
            The current state of the word being guessed, with underscores for unguessed letters.
        attempts_left : int
            The number of attempts the player has left before losing the game.
        game_over_message : str
            A message displayed if the game is over (either won or lost).

        Pygame Documentation:
        ---------------------
        - pygame.Surface.get_rect(): Get the rectangular area of the Surface.
          Reference: https://www.pygame.org/docs/ref/surface.html#pygame.Surface.get_rect
        
        - pygame.Surface.blit(): Draw one image onto another.
          Reference: https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit
        
        - pygame.font.Font.render(): Render text into a new Surface.
          Reference: https://www.pygame.org/docs/ref/font.html#pygame.font.Font.render
        
        - pygame.display.flip(): Update the full display Surface to the screen.
          Reference: https://www.pygame.org/docs/ref/display.html#pygame.display.flip
        """
        self.screen.fill(self.background_color)
        
        # Draw the word with underscores
        word_surface = self.font.render(word, True, self.text_color)
        word_rect = word_surface.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2 - 50))
        self.screen.blit(word_surface, word_rect)
        
        # Draw the number of attempts left
        attempts_surface = self.font.render(f"Attempts Left: {attempts_left}", True, self.text_color)
        attempts_rect = attempts_surface.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2 - 100))
        self.screen.blit(attempts_surface, attempts_rect)
        
        # Draw the game over message if applicable
        if game_over_message:
            message_surface = self.font.render(game_over_message, True, self.text_color)
            message_rect = message_surface.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2 + 150))
            self.screen.blit(message_surface, message_rect)

        self.draw_buttons()
        pygame.display.flip()

    def draw_buttons(self):
        """
        Draws the Start and Quit buttons on the screen.

        This method calculates the positions and sizes of the buttons dynamically
        based on the screen size, then draws them and adds them to the buttons dictionary.

        Pygame Documentation:
        ---------------------
        - pygame.Rect(): Create a rectangle object for positioning and sizing.
          Reference: https://www.pygame.org/docs/ref/rect.html#pygame.Rect
        
        - pygame.draw.rect(): Draw a rectangle shape on the Surface.
          Reference: https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect
        
        - pygame.font.Font.render(): Render text into a new Surface.
          Reference: https://www.pygame.org/docs/ref/font.html#pygame.font.Font.render
        
        - pygame.Surface.blit(): Draw one image onto another.
          Reference: https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit
        """
        screen_width, screen_height = self.screen.get_size()
        button_width = screen_width // 4
        button_height = screen_height // 12
        y_position = screen_height // 2

        # Start Button
        start_x_position = (screen_width - button_width) // 2
        self.buttons['start'] = pygame.Rect(start_x_position, y_position, button_width, button_height)
        pygame.draw.rect(self.screen, self.button_color, self.buttons['start'])
        start_text = self.font.render("Start Game", True, self.text_color)
        self.screen.blit(start_text, (start_x_position + (button_width - start_text.get_width()) // 2, y_position + (button_height - start_text.get_height()) // 2))

        # Quit Button
        quit_x_position = (screen_width - button_width) // 2
        self.buttons['quit'] = pygame.Rect(quit_x_position, y_position + button_height + 20, button_width, button_height)
        pygame.draw.rect(self.screen, self.button_color, self.buttons['quit'])
        quit_text = self.font.render("Quit", True, self.text_color)
        self.screen.blit(quit_text, (quit_x_position + (button_width - quit_text.get_width()) // 2, y_position + button_height + 20 + (button_height - quit_text.get_height()) // 2))

    def display_message(self, message: str, position=None):
        """
        Displays a centered message on the screen.

        Parameters:
        ----------
        message : str
            The message to be displayed.
        position : tuple, optional
            The (x, y) position where the message should be centered. If not provided,
            the message will be centered at the top quarter of the screen.

        Pygame Documentation:
        ---------------------
        - pygame.Surface.get_size(): Get the size of the Surface.
          Reference: https://www.pygame.org/docs/ref/surface.html#pygame.Surface.get_size
        
        - pygame.font.Font.render(): Render text into a new Surface.
          Reference: https://www.pygame.org/docs/ref/font.html#pygame.font.Font.render
        
        - pygame.Surface.get_rect(): Get the rectangular area of the Surface.
          Reference: https://www.pygame.org/docs/ref/surface.html#pygame.Surface.get_rect
        
        - pygame.Surface.blit(): Draw one image onto another.
          Reference: https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit
        """
        if position is None:
            screen_width, screen_height = self.screen.get_size()
            position = (screen_width // 2, screen_height // 4)
        
        message_surface = self.font.render(message, True, self.text_color)
        message_rect = message_surface.get_rect(center=position)
        self.screen.blit(message_surface, message_rect)

    def check_button_click(self, position):
        """
        Checks if a button was clicked based on the mouse position.

        Parameters:
        ----------
        position : tuple
            The (x, y) position of the mouse click.

        Returns:
        -------
        str or None
            The name of the button clicked ('start' or 'quit') or None if no button was clicked.

        Pygame Documentation:
        ---------------------
        - pygame.Rect.collidepoint(): Test if a point is inside the rectangle.
          Reference: https://www.pygame.org/docs/ref/rect.html#pygame.Rect.collidepoint
        """
        for button_name, button_rect in self.buttons.items():
            if button_rect.collidepoint(position):
                return button_name
        return None
