from CheckersModel.checkersModel import CheckersModel
from CheckersModel.gameConstants import WHITE, BLACK, BLANK
from CheckersModel.board import Board


class TestCheckersModel:

    def test_check_move_validity(self):
        cm = CheckersModel()

        assert cm.check_move_validity((5, 0)) is True
        assert cm.check_move_validity((2, 1)) is False
        cm.make_move(5, 0, 4, 1)
        assert cm.check_move_validity((2, 1)) is True

    def test_get_all_moves(self):
        cm = CheckersModel()

        assert cm.get_all_moves(WHITE) == [(2, 1, 3, 0),
                                           (2, 1, 3, 2),
                                           (2, 3, 3, 2),
                                           (2, 3, 3, 4),
                                           (2, 5, 3, 4),
                                           (2, 5, 3, 6),
                                           (2, 7, 3, 6)]

        assert cm.get_all_moves(BLACK) == [(5, 0, 4, 1),
                                           (5, 2, 4, 1),
                                           (5, 2, 4, 3),
                                           (5, 4, 4, 3),
                                           (5, 4, 4, 5),
                                           (5, 6, 4, 5),
                                           (5, 6, 4, 7)]

        cm.make_move(2, 1, 3, 0)

        assert cm.get_all_moves(WHITE) == [(1, 0, 2, 1),
                                           (1, 2, 2, 1),
                                           (2, 3, 3, 2),
                                           (2, 3, 3, 4),
                                           (2, 5, 3, 4),
                                           (2, 5, 3, 6),
                                           (2, 7, 3, 6),
                                           (3, 0, 4, 1)]

    def test_check_winner(self):
        cm = CheckersModel()
        b = Board()
        end_board_string = "⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ " \
                           "⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ " \
                           "⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ " \
                           "⬜  ⬜  ⬜  ⬜  ⬜  ⬜  ⬜  ⬜ " \
                           "⬜  ⬜  ⬜  ⬜  ⬜  ⬜  ⬜  ⬜ " \
                           "B ⬜ B ⬜ B ⬜ B ⬜ " \
                           "⬜ B ⬜ B ⬜ B ⬜ B " \
                           "B ⬜ B ⬜ B ⬜ B ⬜ "
        end_board = b.board_from_string(end_board_string)

        assert cm.check_winner() == BLANK

        cm.board = end_board
        cm.white_pieces = 0

        assert cm.check_winner() is BLACK

    def test_get_turn(self):
        cm = CheckersModel()

        assert cm.get_turn() is True

        cm.make_move(5, 0, 4, 1)

        assert cm.get_turn() is False

    def test_king_pieces(self):
        cm = CheckersModel()
        king_board_before = "⬜ B ⬜ W ⬜ W ⬜ W " \
                            "W ⬜ W ⬜ W ⬜ W ⬜ " \
                            "⬜ W ⬜ W ⬜ W ⬜ W " \
                            "⬜  ⬜  ⬜  ⬜  ⬜  ⬜  ⬜  ⬜ " \
                            "⬜  ⬜  ⬜  ⬜  ⬜  ⬜  ⬜  ⬜ " \
                            "B ⬜ B ⬜ B ⬜ B ⬜ " \
                            "⬜ B ⬜ B ⬜ B ⬜ B " \
                            "W ⬜ B ⬜ B ⬜ B ⬜ "

        b = Board()
        board_before = b.board_from_string(king_board_before)

        cm.board = board_before

        assert cm.get_game_string()[1:5] == '⬜ B '
        assert cm.get_game_string()[-17:-1] == 'W ⬜ B ⬜ B ⬜ B ⬜ '

        cm.king_pieces()

        assert cm.get_game_string()[1:5] == '⬜ Bk'
        assert cm.get_game_string()[-18:-1] == 'Wk ⬜ B ⬜ B ⬜ B ⬜ '

    def test_make_move(self):
        cm = CheckersModel()

        assert cm.get_game_string()[35:68] == '⬜ W ⬜ W ⬜ W ⬜ W\n' \
                                              ' ⬜  ⬜  ⬜  ⬜  ⬜  ⬜'
        cm.make_move(2, 1, 3, 0)
        assert cm.get_game_string()[35:68] == '⬜  ⬜  ⬜ W ⬜ W ⬜ W\n' \
                                              'W ⬜  ⬜  ⬜  ⬜  ⬜'






