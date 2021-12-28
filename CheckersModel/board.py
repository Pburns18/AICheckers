from .gameConstants import ROWS, COLS, WHITE, BLACK, BLANK
from .piece import Piece

"""
Scrap the whole idea about looking multiple moves into the feature.
Instead do the thing w move making and logic. If normal move then switch. Else if capture don't switch.
Unless there are no double jumps to be made. Then switch sort of thing.
we can just make them one at a time. An online checkers website that does this is checkers365 or 
something like that. Just google multiplayer chess"""


class Board:

    def __init__(self, blank=False):
        self.board = [[BLANK] * ROWS for i in range(COLS)]
        if blank is False:
            self.initialize_board()

    def initialize_board(self):
        for row in range(ROWS):
            for col in range(COLS):
                # Handling white pieces
                if row < 3:
                    if row % 2 == 0:
                        if col % 2 == 0:
                            self.board[row][col] = BLANK
                        else:
                            self.board[row][col] = Piece(row, col, WHITE)
                    else:
                        if col % 2 == 1:
                            self.board[row][col] = BLANK
                        else:
                            self.board[row][col] = Piece(row, col, WHITE)
                # Handling black pieces
                elif row > 4:
                    if row % 2 == 0:
                        if col % 2 == 0:
                            self.board[row][col] = BLANK
                        else:
                            self.board[row][col] = Piece(row, col, BLACK)
                    else:
                        if col % 2 == 1:
                            self.board[row][col] = BLANK
                        else:
                            self.board[row][col] = Piece(row, col, BLACK)

    def get_valid_moves(self, row, col):
        # If the passed location is not a piece
        if self.board[row][col] == BLANK:
            return []

        valid_moves = self.get_normal_moves(row, col)
        capture_moves = self.get_capture_moves(row, col)

        valid_moves.extend(capture_moves)

        return valid_moves

    def check_bounds(self, move):
        """Returns True if move is within bounds of board"""
        return 0 <= move[0] < ROWS and 0 <= move[1] < COLS

    def get_capture_moves(self, row, col):
        piece = self.board[row][col]
        color = piece.color
        valid_moves = []
        possible_moves = []

        if piece.king:
            possible_moves.extend([(row - 2, col - 2, row - 1, col - 1), (row - 2, col + 2, row - 1, col + 1),
                                   (row + 2, col - 2, row + 1, col - 1), (row + 2, col + 2, row + 1, col + 1)])

        elif not piece.king:
            if color == WHITE:
                possible_moves.extend([(row + 2, col - 2, row + 1, col - 1), (row + 2, col + 2, row + 1, col + 1)])

            elif color == BLACK:
                possible_moves.extend([(row - 2, col - 2, row - 1, col - 1), (row - 2, col + 2, row - 1, col + 1)])

        for move in possible_moves:
            actual_move = (move[0], move[1])
            captured_space = (move[2], move[3])
            if not self.check_bounds(actual_move) or not self.check_bounds(captured_space):
                continue
            # Case where there is nothing to hop over
            if self.is_empty(captured_space[0], captured_space[1]):
                continue
            if self.valid_capture(captured_space, actual_move, color):
                valid_moves.append(actual_move)

        return valid_moves

    def capture_piece(self, row, col):
        self.board[row][col] = BLANK

    def valid_capture(self, capture_space, move_space, color):
        return color != self.board[capture_space[0]][capture_space[1]].color \
               and self.is_empty(move_space[0], move_space[1])

    def get_normal_moves(self, row, col):
        # Given the row / column of the piece this method will return all valid moves
        piece = self.board[row][col]
        color = piece.color
        valid_moves = []
        possible_moves = []

        # Case 1: King moves
        # Check location row +- 1, col +- 1
        if piece.king:
            possible_moves.extend([(row - 1, col - 1), (row - 1, col + 1), (row + 1, col - 1), (row + 1, col + 1)])

        elif not piece.king:
            # Case 2: Normal forward moves
            if color == WHITE:
                # Check location row + 1, col +-1
                possible_moves.extend([(row + 1, col - 1), (row + 1, col + 1)])

            elif color == BLACK:
                # Check location row - 1, col +- 1
                possible_moves.extend([(row - 1, col - 1), (row - 1, col + 1)])

        for move in possible_moves:
            # print(f'{move}, {self.is_empty(move[0], move[1])}')
            if not self.check_bounds(move):
                continue
            if self.is_empty(move[0], move[1]):
                valid_moves.append(move)

        return valid_moves

    def move_piece(self, row_from, col_from, row_to, col_to):
        """ Case 1: Simple move - diagonal space forward is empty
            Case 2: King move - diagonal space forward and backwards is empty
            Case 3: Jumping move - piece of opposite color on diagonal - if room
            allows able to advance another row can jump and capture"""

        # Update the piece
        self.board[row_from][col_from].move_piece(row_to, col_to)

        # Moving the piece on the board
        self.board[row_to][col_to], self.board[row_from][col_from] = self.board[row_from][col_from], BLANK

    def is_empty(self, row, col):
        """This method returns True if the square in question (row, col) is empty.
        Or if the square in question contains a piece which does not have the supplied color.

        Purpose: Able to check if the a square has certain color piece"""

        return self.board[row][col] == BLANK

    def contains_piece(self, row, col, color):
        return self.board[row][col].color == color

    def king_pieces(self):
        for square in self.board[0]:
            if square == BLANK:
                continue
            else:
                if square.color == BLACK:
                    square.king_piece()

        for square in self.board[ROWS - 1]:
            if square == BLANK:
                continue
            else:
                if square.color == WHITE:
                    square.king_piece()

    def board_from_string(self, board_string):
        row = 0
        col = 0
        new_board = Board(blank=True)
        board_string = board_string.replace('  ', ' ')
        board_string = board_string.replace('\n', ' ')
        board_string = board_string.split(' ')
        t = ''
        for char in board_string:
            t += char
            if row == ROWS:
                return new_board
            elif char == 'W':
                new_board.board[row][col] = Piece(row, col, WHITE)
            elif char == 'Wk':
                new_board.board[row][col] = Piece(row, col, WHITE).king_piece()
            elif char == 'B':
                new_board.board[row][col] = Piece(row, col)
            elif char == 'Bk':
                new_board.board[row][col] = Piece(row, col).king_piece()
            elif char == '⬜':
                new_board.board[row][col] == Piece(row, col, BLANK)
            else:
                continue

            col += 1

            if col == COLS:
                row += 1
                col = 0

        return new_board

    def __repr__(self, text=False):
        t = ''
        if text is False:
            return self.board
        else:
            for row in range(ROWS):
                if t != '':
                    t += '\n'
                for col in range(COLS):
                    t += self.board[row][col].__repr__()

        return t
