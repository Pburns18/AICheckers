from abc import ABC, abstractmethod


class ACheckersModel(ABC):
    """Represents an abstract class for the model of a Checkers game."""

    @abstractmethod
    def get_game_string(self):
        """Returns the string board representation of the Checkers game state

        Returns:
            game_string : String - Text representation of game state"""
        pass

    @abstractmethod
    def get_all_moves(self, color):
        """Gets and returns a list of all valid moves on a board for the specified
        color.

        Args:
            color : (int, int, int) - RGB Representation of color to get moves for

        Returns:
            move_set : [(int, int, int, int)] - List of moves in Tuple form. Following the
            format of (row_from, col_from, row_to, col_to) which represents the move starting
            location in row/column form and the move ending space in row/column form"""
        pass

    @abstractmethod
    def check_winner(self):
        """Checks the checkers model to see if their is a winner. Win conditions -
        either player has 0 pieces left - in which opposite player wins. Or a player
        has no valid moves - in which the opposite player also wins.

        Returns:
            winner : (int, int, int) - RGB Representation of winner
                (0, 0, 0) - Black winner
                (255, 255, 255) - White winner
                (128, 128, 128) - Grey/Blank = No current winner"""
        pass

    @abstractmethod
    def get_turn(self):
        """Gets which player/color which turn it currently is. If false - White turn
        If True - Black turn

        Returns:
            turn : bool - True if Black turn, else False and White turn."""
        pass

    @abstractmethod
    def king_pieces(self):
        """Alters the game state and board so that pieces which should be 'kings' are
        made to be kings. Typically in checkers this occurs when a piece has reached
        the last row on the opponents side of the board."""
        pass

    @abstractmethod
    def make_move(self, row_from, col_from, row_to, col_to):
        """Alters the checkers model by making a piece move from the 'from' location
        to the 'to' location - both supplied in row/column form. Logic for whether the move
        is a normal move or capture move is baked into this function. If it is a capture
        the piece will be captured. Else a normal move will be made. Also alters
        the turn state of the model to accurately follow the implemented rules of checkers.

        Args:
            row_from : int - Represents the row value of the starting move location
            col_from : int - Represents the column value of the starting move location
            row_to : int - Represents the row value of the ending move location
            col_to : int - Represents the column value of the ending move location"""
        pass
