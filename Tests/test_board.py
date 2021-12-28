from CheckersModel.board import Board
from CheckersModel.piece import Piece
from CheckersModel.gameConstants import WHITE, BLACK, BLANK


class TestBoard:

    def test_board_string(self):
        test_board = "⬜ W ⬜ W ⬜ W ⬜ W " \
                     "W ⬜ W ⬜ W ⬜ W ⬜ " \
                     "⬜ W ⬜ W ⬜ W ⬜ W " \
                     "⬜  ⬜  ⬜  ⬜  ⬜  ⬜  ⬜  ⬜ " \
                     "⬜  ⬜  ⬜  ⬜  ⬜  ⬜  ⬜  ⬜ " \
                     "B ⬜ B ⬜ B ⬜ B ⬜ " \
                     "⬜ B ⬜ B ⬜ B ⬜ B " \
                     "B ⬜ B ⬜ B ⬜ B ⬜ "

        b = Board()
        converted = b.board_from_string(board_string=test_board)

        assert b.__repr__(text=True) == converted.__repr__(text=True)

    def test_board_init(self):
        b = Board()

        # Picking known spots on board to ensure correct pieces are being generated
        # during the init

        assert b.__getattribute__('board')[0][0].__repr__() == '\'⬜\''
        assert b.__getattribute__('board')[0][1].__repr__() == 'W'
        assert b.__getattribute__('board')[5][0].__repr__() == 'B'

    def test_get_valid_moves(self):
        # get_valid_moves returns valid moves based on the supplied row/column pair
        # Will return moves regardless of which players turn it is in the game state
        b = Board()

        assert b.get_valid_moves(0, 0) == []
        assert b.get_valid_moves(2, 1) == [(3, 0), (3, 2)]
        assert b.get_valid_moves(5, 0) == [(4, 1)]

    def test_check_bounds(self):
        b = Board()

        assert b.check_bounds((0, 0)) is True
        assert b.check_bounds((7, 7)) is True
        assert b.check_bounds((8, 2)) is False
        assert b.check_bounds((-1, 0)) is False

    def test_get_capture_moves(self):
        b = Board()
        capture_string_w = \
            "⬜ W ⬜ W ⬜ W ⬜ W " \
            "W ⬜ W ⬜ W ⬜ W ⬜ " \
            "⬜ ⬜ ⬜ ⬜ ⬜ W ⬜ W " \
            "⬜  ⬜  W  ⬜  ⬜  ⬜  ⬜  ⬜ " \
            "⬜  B  ⬜  ⬜  ⬜  ⬜  ⬜  ⬜ " \
            "⬜ ⬜ ⬜ ⬜ B ⬜ B ⬜ " \
            "⬜ B ⬜ B ⬜ B ⬜ B " \
            "B ⬜ B ⬜ B ⬜ B ⬜ "
        capture_string_b = \
            "⬜ W ⬜ W ⬜ W ⬜ W " \
            "W ⬜ W ⬜ W ⬜ W ⬜ " \
            "⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ W " \
            "⬜  W  ⬜  W  ⬜  ⬜  ⬜  ⬜ " \
            "⬜  ⬜  B  ⬜  ⬜  ⬜  ⬜  ⬜ " \
            "B ⬜ ⬜ B B ⬜ B ⬜ " \
            "⬜ B ⬜ B ⬜ B ⬜ B " \
            "B ⬜ B ⬜ B ⬜ B ⬜ "
        capture_bw = b.board_from_string(capture_string_w)
        capture_bb = b.board_from_string(capture_string_b)

        assert capture_bw.get_capture_moves(0, 1) == []
        assert capture_bw.get_capture_moves(3, 2) == [(5, 0)]
        assert capture_bb.get_capture_moves(4, 2) == [(2, 0), (2, 4)]
        assert capture_bb.get_capture_moves(3, 1) == []

    def test_capture_piece(self):
        b = Board()
        capture_string_w = \
            "⬜ W ⬜ W ⬜ W ⬜ W " \
            "W ⬜ W ⬜ W ⬜ W ⬜ " \
            "⬜ ⬜ ⬜ ⬜ ⬜ W ⬜ W " \
            "⬜  ⬜  W  ⬜  ⬜  ⬜  ⬜  ⬜ " \
            "⬜  B  ⬜  ⬜  ⬜  ⬜  ⬜  ⬜ " \
            "⬜ ⬜ ⬜ ⬜ B ⬜ B ⬜ " \
            "⬜ B ⬜ B ⬜ B ⬜ B " \
            "B ⬜ B ⬜ B ⬜ B ⬜ "
        capture_string_b = \
            "⬜ W ⬜ W ⬜ W ⬜ W " \
            "W ⬜ W ⬜ W ⬜ W ⬜ " \
            "⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ W " \
            "⬜  W  ⬜  W  ⬜  ⬜  ⬜  ⬜ " \
            "⬜  ⬜  B  ⬜  ⬜  ⬜  ⬜  ⬜ " \
            "B ⬜ ⬜ B B ⬜ B ⬜ " \
            "⬜ B ⬜ B ⬜ B ⬜ B " \
            "B ⬜ B ⬜ B ⬜ B ⬜ "
        capture_bw = b.board_from_string(capture_string_w)
        capture_bb = b.board_from_string(capture_string_b)

        capture_bw.capture_piece(3, 2)
        capture_bb.capture_piece(4, 2)

        assert capture_bw.board[3][2] == BLANK
        assert capture_bb.board[4][2] == BLANK

    def test_valid_capture(self):
        b = Board()
        capture_string_w = \
            "⬜ W ⬜ W ⬜ W ⬜ W " \
            "W ⬜ W ⬜ W ⬜ W ⬜ " \
            "⬜ ⬜ ⬜ ⬜ ⬜ W ⬜ W " \
            "⬜  ⬜  W  ⬜  ⬜  ⬜  ⬜  ⬜ " \
            "⬜  B  ⬜  ⬜  ⬜  ⬜  ⬜  ⬜ " \
            "⬜ ⬜ ⬜ ⬜ B ⬜ B ⬜ " \
            "⬜ B ⬜ B ⬜ B ⬜ B " \
            "B ⬜ B ⬜ B ⬜ B ⬜ "
        capture_string_b = \
            "⬜ W ⬜ W ⬜ W ⬜ W " \
            "W ⬜ W ⬜ W ⬜ W ⬜ " \
            "⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ W " \
            "⬜  W  ⬜  W  ⬜  ⬜  ⬜  ⬜ " \
            "⬜  ⬜  B  ⬜  ⬜  ⬜  ⬜  ⬜ " \
            "B ⬜ ⬜ B B ⬜ B ⬜ " \
            "⬜ B ⬜ B ⬜ B ⬜ B " \
            "B ⬜ B ⬜ B ⬜ B ⬜ "
        capture_bw = b.board_from_string(capture_string_w)
        capture_bb = b.board_from_string(capture_string_b)

        assert capture_bw.valid_capture((4, 1), (5, 0), WHITE) is True
        assert capture_bb.valid_capture((3, 1), (2, 0), BLACK) is True
        assert capture_bb.valid_capture((3, 3), (2, 4), BLACK) is True
        assert capture_bb.valid_capture((3, 3), (2, 4), WHITE) is False

    def test_get_normal_moves(self):
        test_board = "⬜ W ⬜ W ⬜ W ⬜ W " \
                     "W ⬜ W ⬜ W ⬜ W ⬜ " \
                     "⬜ W ⬜ W ⬜ W ⬜ W " \
                     "⬜  ⬜  ⬜  ⬜  ⬜  ⬜  ⬜  ⬜ " \
                     "⬜  ⬜  ⬜  ⬜  ⬜  ⬜  ⬜  ⬜ " \
                     "B ⬜ B ⬜ B ⬜ B ⬜ " \
                     "⬜ B ⬜ B ⬜ B ⬜ B " \
                     "B ⬜ B ⬜ B ⬜ B ⬜ "
        capture_string_w = \
            "⬜ W ⬜ W ⬜ W ⬜ W " \
            "W ⬜ W ⬜ W ⬜ W ⬜ " \
            "⬜ ⬜ ⬜ ⬜ ⬜ W ⬜ W " \
            "⬜  ⬜  W  ⬜  ⬜  ⬜  ⬜  ⬜ " \
            "⬜  B  ⬜  ⬜  ⬜  ⬜  ⬜  ⬜ " \
            "⬜ ⬜ ⬜ ⬜ B ⬜ B ⬜ " \
            "⬜ B ⬜ B ⬜ B ⬜ B " \
            "B ⬜ B ⬜ B ⬜ B ⬜ "

        b = Board()
        normal_board = b.board_from_string(test_board)
        capture_bw = b.board_from_string(capture_string_w)

        assert normal_board.get_normal_moves(2, 1) == [(3, 0), (3, 2)]
        assert normal_board.get_normal_moves(5, 0) == [(4, 1)]
        assert capture_bw.get_normal_moves(3, 2) == [(4, 3)]

    def test_move_piece(self):
        test_board = "⬜ W ⬜ W ⬜ W ⬜ W " \
                     "W ⬜ W ⬜ W ⬜ W ⬜ " \
                     "⬜ W ⬜ W ⬜ W ⬜ W " \
                     "⬜  ⬜  ⬜  ⬜  ⬜  ⬜  ⬜  ⬜ " \
                     "⬜  ⬜  ⬜  ⬜  ⬜  ⬜  ⬜  ⬜ " \
                     "B ⬜ B ⬜ B ⬜ B ⬜ " \
                     "⬜ B ⬜ B ⬜ B ⬜ B " \
                     "B ⬜ B ⬜ B ⬜ B ⬜ "
        b = Board()
        normal_board = b.board_from_string(test_board)

        normal_board.move_piece(2, 1, 3, 0)
        normal_board.move_piece(5, 0, 4, 1)

        assert normal_board.board[2][1].__repr__() == '\'⬜\''
        assert normal_board.board[3][0].__repr__() == Piece(3, 0, WHITE).__repr__()
        assert normal_board.board[5][0].__repr__() == '\'⬜\''
        assert normal_board.board[4][1].__repr__() == Piece(4, 1, BLACK).__repr__()

    def test_is_empty(self):
        test_board = "⬜ W ⬜ W ⬜ W ⬜ W " \
                     "W ⬜ W ⬜ W ⬜ W ⬜ " \
                     "⬜ W ⬜ W ⬜ W ⬜ W " \
                     "⬜  ⬜  ⬜  ⬜  ⬜  ⬜  ⬜  ⬜ " \
                     "⬜  ⬜  ⬜  ⬜  ⬜  ⬜  ⬜  ⬜ " \
                     "B ⬜ B ⬜ B ⬜ B ⬜ " \
                     "⬜ B ⬜ B ⬜ B ⬜ B " \
                     "B ⬜ B ⬜ B ⬜ B ⬜ "
        b = Board()
        normal_board = b.board_from_string(test_board)

        assert normal_board.is_empty(0, 0) is True
        assert normal_board.is_empty(1, 0) is False
        assert normal_board.is_empty(5, 0) is False

    def test_contains_piece(self):
        test_board = "⬜ W ⬜ W ⬜ W ⬜ W " \
                     "W ⬜ W ⬜ W ⬜ W ⬜ " \
                     "⬜ W ⬜ W ⬜ W ⬜ W " \
                     "⬜  ⬜  ⬜  ⬜  ⬜  ⬜  ⬜  ⬜ " \
                     "⬜  ⬜  ⬜  ⬜  ⬜  ⬜  ⬜  ⬜ " \
                     "B ⬜ B ⬜ B ⬜ B ⬜ " \
                     "⬜ B ⬜ B ⬜ B ⬜ B " \
                     "B ⬜ B ⬜ B ⬜ B ⬜ "
        b = Board()
        normal_board = b.board_from_string(test_board)

        assert normal_board.contains_piece(1, 0, WHITE) is True
        assert normal_board.contains_piece(5, 0, BLACK) is True

    def test_king_pieces(self):
        king_board_before = "⬜ B ⬜ W ⬜ W ⬜ W " \
                            "W ⬜ W ⬜ W ⬜ W ⬜ " \
                            "⬜ W ⬜ W ⬜ W ⬜ W " \
                            "⬜  ⬜  ⬜  ⬜  ⬜  ⬜  ⬜  ⬜ " \
                            "⬜  ⬜  ⬜  ⬜  ⬜  ⬜  ⬜  ⬜ " \
                            "B ⬜ B ⬜ B ⬜ B ⬜ " \
                            "⬜ B ⬜ B ⬜ B ⬜ B " \
                            "W ⬜ B ⬜ B ⬜ B ⬜ "

        king_board_after = "⬜ Bk ⬜ W ⬜ W ⬜ W " \
                           "W ⬜ W ⬜ W ⬜ W ⬜ " \
                           "⬜ W ⬜ W ⬜ W ⬜ W " \
                           "⬜  ⬜  ⬜  ⬜  ⬜  ⬜  ⬜  ⬜ " \
                           "⬜  ⬜  ⬜  ⬜  ⬜  ⬜  ⬜  ⬜ " \
                           "B ⬜ B ⬜ B ⬜ B ⬜ " \
                           "⬜ B ⬜ B ⬜ B ⬜ B " \
                           "Wk ⬜ B ⬜ B ⬜ B ⬜ "

        b = Board()
        board_before = b.board_from_string(king_board_before)
        board_after = b.board_from_string(king_board_after)

        assert board_before != board_after
        board_before.king_pieces()
        assert board_after == board_after
