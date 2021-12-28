from abc import ABC, abstractmethod


class ACheckersView(ABC):
    """Represents an abstract class for a View for a game of checkers. The view
    handles the visual representation of the game. Can come in many forms such as Text,
    gui, etc. The view handles displaying the board, which player's turn it is, score or state
    of the game, as well as the winner"""

    @abstractmethod
    def show_board(self, board):
        """Displays the board and its pieces via the views method of display. Does
        this using the supplied board which contains pieces

        Args:
            board : [[Piece]] - 2D Array of pieces representing a checkers board"""
        pass

    @abstractmethod
    def show_score(self, black, white, move):
        """Displays the current score (# of pieces for each player) as well as
        which players turn it is.

        Args:
            black : int - Number of pieces remaining for black
            white : int - Number of pieces remaining for white
            move : bool - True = black turn - False = white turn"""
        pass

    @abstractmethod
    def show_winner(self, winner):
        """Displays the winner of the game when a winner is determined.

        Args:
            winner : String - String representation of which player won"""
        pass

    @abstractmethod
    def close_view(self):
        """Closes the display or displays an ending message"""
        pass

    @abstractmethod
    def prompt_user(self, black_move):
        """Prompts the user to make a move.

        Args:
            black_move : bool - True of Black turn - False if White turn"""
        pass

    @abstractmethod
    def show_move(self, row_from, col_from, row_to, col_to):
        """Displays the move being made.

        Args:
            row_from, col_from, row_to, col_to : (int, int, int, int) - representing
            a move to be made in the game of checkers"""
        pass
