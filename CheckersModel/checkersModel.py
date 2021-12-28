from CheckersModel import board, gameConstants
from CheckersModel.ACheckersModel import ACheckersModel
from .gameConstants import WHITE, BLACK, BLANK


class CheckersModel(ACheckersModel):

    def __init__(self):
        self.board = board.Board()
        self.white_pieces = 12
        self.black_pieces = 12
        self.white_kings = 0
        self.black_kings = 0
        self.black_move = True
        self.last_move = None

    def get_game_string(self):
        game_string = ""
        for row in self.board.board:
            row_string = ""
            for piece in row:
                if piece != gameConstants.BLANK:
                    row_string += piece.__repr__()
                else:
                    row_string += " "
                    row_string += gameConstants.BLANK
                    row_string += " "
            game_string += row_string
            game_string += "\n"

        return game_string

    def check_move_validity(self, move):
        if self.black_move and self.board.board[move[0]][move[1]].color == BLACK:
            return True
        elif not self.black_move and self.board.board[move[0]][move[1]].color == WHITE:
            return True
        else:
            return False

    def get_all_moves(self, color):
        move_set = []
        if self.last_move is None:
            b = self.board
            possible_moves = []
            for row in b.board:
                for piece in row:
                    if piece == BLANK:
                        continue
                    if piece.color == color:
                        moves = b.get_valid_moves(piece.row, piece.col)
                        moves = [(piece.row, piece.col, move[0], move[1]) for move in moves]
                        possible_moves.append(moves)
                        possible_moves = [move for move in possible_moves if move != []]
                        move_set = [item for sublist in possible_moves for item in sublist]
        else:
            # This is the case where we have a last capture move
            b = self.board
            moves = b.get_capture_moves(self.last_move[0], self.last_move[1])
            move_set = [(self.last_move[0], self.last_move[1], item[0], item[1]) for item in moves]

        return move_set

    def check_winner(self):
        if self.white_pieces == 0:
            return BLACK
        elif self.black_pieces == 0:
            return WHITE
        else:
            return BLANK

    def get_turn(self):
        return self.black_move

    def king_pieces(self):
        self.board.king_pieces()

    def make_move(self, row_from, col_from, row_to, col_to):
        if self.last_move is None:
            valid_moves_from = self.board.get_valid_moves(row_from, col_from)
        else:
            valid_moves_from = self.board.get_capture_moves(self.last_move[0], self.last_move[1])

        if len(valid_moves_from) == 0:
            return

        if (row_to, col_to) in valid_moves_from:
            # This means we are capturing a piece - we do not flip the turn - only if there are no moves left
            if abs(row_from - row_to) + abs(col_from - col_to) == 4:
                self.board.capture_piece(int((row_from + row_to) / 2), int((col_from + col_to) / 2))
                if self.black_move:
                    self.white_pieces -= 1
                else:
                    self.black_pieces -= 1
                self.board.move_piece(row_from, col_from, row_to, col_to)
                self.king_pieces()
                self.last_move = (row_to, col_to)

                # If we are making a capture - we check to see if there are more captures to be made from
                # the new location. If there are. Then we do not switch turns. Else we do
                if len(self.board.get_capture_moves(row_to, col_to)) == 0:
                    self.black_move = not self.black_move
                    self.last_move = None

            # This means we are making a normal move - we flip the turn
            else:
                self.last_move = None
                self.board.move_piece(row_from, col_from, row_to, col_to)
                self.king_pieces()
                self.black_move = not self.black_move
