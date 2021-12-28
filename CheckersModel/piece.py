from .gameConstants import BLACK, BOARD_DIM, ROWS, COLS


class Piece:

    def __init__(self, row, col, color=BLACK):
        self.color = color
        self.row = row
        self.col = col
        self.x = 0
        self.y = 0
        self.init_pos()
        self.king = False

    def init_pos(self):
        # Calculates top left corner for x, y pos based on rows and cols
        self.x = BOARD_DIM / ROWS * self.row
        self.y = BOARD_DIM / COLS * self.col

    def move_piece(self, row_to, col_to):
        self.row = row_to
        self.col = col_to
        self.init_pos()

    def king_piece(self):
        self.king = True

    def __repr__(self, debug=False):
        if debug:
            return f'({self.row}, {self.col}) '
        if self.color == (255, 255, 255):
            if self.king:
                return 'Wk'
            else:
                return 'W'
        else:
            if self.king:
                return 'Bk'
            else:
                return 'B'
