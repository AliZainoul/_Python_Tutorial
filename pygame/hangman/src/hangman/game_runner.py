import pygame
from hangman import Hangman
from controller.hangman_controller import HangmanController
from ui.gui import GUI


class GameRunner:
    """
    The GameRunner class encapsulates the initialization and running of the Hangman game.

    This class sets up the Pygame environment, initializes the screen, font, GUI (view),
    the Hangman game logic (model), and the HangmanController (controller) that handles
    the interaction between the model and view.

    Attributes:
    ----------
    screen : pygame.Surface
        The display surface where the game graphics are rendered.
    font : pygame.font.Font
        The font used for displaying text in the game.
    view : GUI
        The graphical user interface for the game.
    model : Hangman
        The core logic of the Hangman game.
    controller : HangmanController
        The controller that manages the game logic and updates the view.
    """

    def __init__(self):
        """
        Initializes the Pygame environment, screen, font, GUI, model, and controller.

        This constructor sets up the necessary components for running the Hangman game.

        Pygame Documentation:
        ---------------------
        - pygame.init(): Initializes all imported Pygame modules.
          Reference: https://www.pygame.org/docs/ref/pygame.html#pygame.init
        
        - pygame.display.set_mode(size, flags=0): Initializes a window or screen for display.
          - size: (width, height) tuple for the dimensions of the screen. 
          - flags: Additional options (e.g., pygame.RESIZABLE, pygame.FULLSCREEN).
          Reference: https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode
        
        - pygame.font.SysFont(name, size): Creates a Font object from system fonts.
          - name: Name of the system font to use (None to use the default).
          - size: The height of the font in pixels.
          Reference: https://www.pygame.org/docs/ref/font.html#pygame.font.SysFont
        """
        pygame.init()

        # Set up the screen and font
        self.screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
        """
        Initializes the screen with the given dimensions and flags.

        Parameters:
        ----------
        size : tuple
            The width and height of the screen in pixels (e.g., (800, 600)).
        flags : int, optional
            Additional options for the display mode. Default is 0 (no flags).
            - pygame.RESIZABLE: Allow the window to be resized.
        """

        self.font = pygame.font.SysFont(None, 48)
        """
        Initializes the font used in the game.

        Parameters:
        ----------
        name : str or None
            The name of the system font to use. If None, the default Pygame font is used.
        size : int
            The height of the font in pixels (e.g., 48).
        """

        # Initialize the view (GUI), model (Hangman), and controller (HangmanController)
        self.view = GUI(self.screen, self.font)
        self.model = Hangman(['python', 'hangman', 'example'])
        self.controller = HangmanController(self.model, self.view)

    def run(self):
        """
        Starts the game loop by calling the controller's run_game_loop method.

        This method enters the main game loop, where the game logic is continuously
        processed, and the screen is updated accordingly.

        Pygame Documentation:
        ---------------------
        - pygame.display.update(): Updates the entire display.
          Reference: https://www.pygame.org/docs/ref/display.html#pygame.display.update
        """
        self.controller.run_game_loop()

    def __del__(self):
        """
        Cleans up the Pygame environment when the GameRunner object is destroyed.

        This method ensures that Pygame quits properly, freeing up any resources it used.

        Pygame Documentation:
        ---------------------
        - pygame.quit(): Uninitialize all Pygame modules and quit the program.
          Reference: https://www.pygame.org/docs/ref/pygame.html#pygame.quit
        """
        pygame.quit()
