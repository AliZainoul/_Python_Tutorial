from game_runner import GameRunner

def main():
    """
    The main function to start the Hangman game.

    This function creates an instance of the GameRunner class 
    and calls its run method to start the game.
    """
    gr = GameRunner()
    gr.run()
    
if __name__ == "__main__":
    main()
