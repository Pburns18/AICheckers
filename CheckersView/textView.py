from CheckersView.ACheckersView import ACheckersView


class TextView(ACheckersView):
    """Represents a View for a Checkers game which will display the game to
    console using text."""

    def show_pieces(self, board_string):
        pass

    def show_board(self, board_string):
        """Prints the state of the board to the console with the supplied string representation
        of the board

        Args:
            board_string : String representation of the board state to draw"""
        print(board_string)
        print()

    def show_score(self, black, white, move):
        """Displays the current score (# of pieces for each player) as well as
        which players turn it is.

        Args:
            black : int - Number of pieces remaining for black
            white : int - Number of pieces remaining for white
            move : bool - True = black turn - False = white turn"""

        print(f'Black has {black} pieces left. \n'
              f'White has {white} pieces left.')

        if move:
            print('Black Turn')
        else:
            print('White Turn')

    def show_winner(self, winner):
        """Displays the winner of the game using the supplied winner.

        Args:
            winner : String - String representing winner of the game"""

        print(f'The winner is {winner}')

    def close_view(self):
        """Closes the display with an ending message"""
        print(f'Come play again soon!')

    def prompt_user(self, black_move):
        """Prompts the user to make a move.

        Args:
            black_move : bool - True of Black turn - False if White turn"""

        if black_move:
            print('Black please enter a move from \'row, col -> row, col\'')
        else:
            print('White please enter a move from \'row, col -> row, col\'')

    def show_move(self, row_from, col_from, row_to, col_to):
        """Displays the move being made.

        Args:
            row_from, col_from, row_to, col_to : (int, int, int, int) - representing
            a move to be made in the game of checkers"""
        print(f'({row_from}, {col_from}) -> ({row_to}, {col_to})')
