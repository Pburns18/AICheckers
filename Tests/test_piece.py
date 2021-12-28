import pytest
from CheckersModel.piece import Piece
from CheckersModel.gameConstants import WHITE


class TestPiece:

    def test_init(self):
        assert Piece(0, 0).__repr__(debug=True) == '(0, 0) '
        assert Piece(0, 0).__repr__() == 'B'
        assert Piece(0, 0, WHITE).__repr__() == 'W'

    def test_king(self):
        w = Piece(0, 0, WHITE)
        w.king_piece()
        b = Piece(1, 1)
        b.king_piece()

        assert w.__repr__() == 'Wk'
        assert b.__repr__() == 'Bk'

    def test_move(self):
        p = Piece(0, 0)
        assert p.__getattribute__('row') == 0
        assert p.__getattribute__('col') == 0
        p.move_piece(4, 2)
        assert p.__getattribute__('row') == 4
        assert p.__getattribute__('col') == 2

    def test_pos(self):
        p = Piece(0, 0)
        p2 = Piece(1, 2)
        assert p.__getattribute__('x') == 0
        assert p.__getattribute__('y') == 0
        assert p2.__getattribute__('x') == 75
        assert p2.__getattribute__('y') == 150


