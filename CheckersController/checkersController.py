import copy
from CheckersModel.gameConstants import BLACK, WHITE, BLANK, BOARD_DIM, ROWS
from CheckersMinimax.minimax import Minimax
import random


class CheckersController:
    """Represents a Controller for a checkers game and serves to connect
    both the model and the view as well as handle User Input and game loop.

    Args:
        model : ACheckersModel - A model for the game of checkers (represents game logic and state)
        view : ACheckersView - A View or GUI for the game of checkers"""

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_board(self):
        game_state = self.model.get_game_string()
        self.view.show_board(game_state)

    @staticmethod
    def get_input():
        row_from = int(input('Row From: '))
        col_from = int(input('Col From: '))
        row_to = int(input('Row To: '))
        col_to = int(input('Col To: '))

        return row_from, col_from, row_to, col_to

    @staticmethod
    def get_move_from_pos(pos):

        size = BOARD_DIM / ROWS

        x1_row = int(pos[0] / size)
        y1_row = int(pos[1] / size)
        x2_row = int(pos[2] / size)
        y2_row = int(pos[3] / size)

        return y1_row, x1_row, y2_row, x2_row

    def play_ai_vs_ai(self, black_depth=2, white_depth=3):
        cm = self.model
        v = self.view

        while cm.check_winner() == BLANK:
            v.show_board(cm.get_game_string())
            v.show_pieces(cm.get_game_string())
            v.show_score(cm.black_pieces, cm.white_pieces, cm.black_move)

            if cm.black_move:
                legal_moves_black = cm.get_all_moves(BLACK)
                if len(legal_moves_black) == 0:
                    return WHITE
                legal_moves_dict = {}
                if legal_moves_black:
                    best_val = float("-inf")
                    mm = Minimax()
                    for move in legal_moves_black:
                        new_model = copy.deepcopy(cm)
                        new_model.make_move(row_from=move[0], col_from=move[1],
                                            row_to=move[2], col_to=move[3])
                        move_value = mm.minimax_value(new_model, black_depth,
                                                      float("-inf"), float("inf"))
                        legal_moves_dict[move] = move_value

                        if move_value > best_val:
                            best_val = move_value

                    best_move = random.choice([move for move, val in legal_moves_dict.items()
                                               if val == best_val])

                    cm.make_move(row_from=best_move[0], col_from=best_move[1],
                                 row_to=best_move[2], col_to=best_move[3])
            else:
                legal_moves = cm.get_all_moves(WHITE)
                if len(legal_moves) == 0:
                    return BLACK
                legal_moves_dict = {}
                if legal_moves:
                    best_val = float("-inf")
                    mm = Minimax()
                    for move in legal_moves:
                        new_model = copy.deepcopy(cm)
                        new_model.make_move(row_from=move[0], col_from=move[1],
                                            row_to=move[2], col_to=move[3])
                        move_value = mm.minimax_value(new_model, white_depth,
                                                      float("-inf"), float("inf"))
                        legal_moves_dict[move] = move_value

                        if move_value > best_val:
                            best_val = move_value

                    best_move = random.choice([move for move, val in legal_moves_dict.items()
                                               if val == best_val])

                    cm.make_move(row_from=best_move[0], col_from=best_move[1],
                                 row_to=best_move[2], col_to=best_move[3])

    def play_ai_vs_random(self):
        cm = self.model
        v = self.view

        while cm.check_winner() == BLANK:
            v.show_board(cm.get_game_string())
            v.show_pieces(cm.get_game_string())
            v.show_score(cm.black_pieces, cm.white_pieces, cm.black_move)
            v.show_move(0, 0, 0, 0)

            if cm.black_move:
                legal_moves_black = cm.get_all_moves(BLACK)
                if len(legal_moves_black) == 0:
                    return WHITE
                random_move = random.choice(legal_moves_black)
                cm.make_move(row_from=random_move[0], col_from=random_move[1],
                             row_to=random_move[2], col_to=random_move[3])
            else:
                legal_moves = cm.get_all_moves(WHITE)
                if len(legal_moves) == 0:
                    return BLACK
                legal_moves_dict = {}
                if legal_moves:
                    best_val = float("-inf")
                    mm = Minimax()
                    for move in legal_moves:
                        new_model = copy.deepcopy(cm)
                        new_model.make_move(row_from=move[0], col_from=move[1],
                                            row_to=move[2], col_to=move[3])
                        move_value = mm.minimax_value(new_model, 2,
                                                      float("-inf"), float("inf"))
                        legal_moves_dict[move] = move_value

                        if move_value > best_val:
                            best_val = move_value

                    best_move = random.choice([move for move, val in legal_moves_dict.items()
                                               if val == best_val])

                    cm.make_move(row_from=best_move[0], col_from=best_move[1],
                                 row_to=best_move[2], col_to=best_move[3])

        return cm.check_winner()

    def play_ai(self, depth=3):
        cm = self.model
        v = self.view

        while cm.check_winner() == BLANK:
            v.show_board(cm.get_game_string())
            v.show_pieces(cm.get_game_string())
            v.show_score(cm.black_pieces, cm.white_pieces, cm.black_move)

            b = cm.board.board
            if cm.black_move:
                pos = v.get_click()
                move = self.get_move_from_pos(pos)
                if b[move[0]][move[1]].color == BLACK:
                    cm.make_move(move[0], move[1], move[2], move[3])
            else:
                legal_moves = cm.get_all_moves(WHITE)
                legal_moves_dict = {}
                if legal_moves:
                    best_val = float("-inf")
                    mm = Minimax()
                    for move in legal_moves:
                        new_model = copy.deepcopy(cm)
                        new_model.make_move(row_from=move[0], col_from=move[1],
                                            row_to=move[2], col_to=move[3])
                        move_value = mm.minimax_value(new_model, depth,
                                                      float("-inf"), float("inf"))
                        legal_moves_dict[move] = move_value

                        if move_value > best_val:
                            best_val = move_value

                    best_move = random.choice([move for move, val in legal_moves_dict.items()
                                               if val == best_val])

                    cm.make_move(row_from=best_move[0], col_from=best_move[1],
                                 row_to=best_move[2], col_to=best_move[3])

    def run_game(self):
        cm = self.model
        v = self.view

        while cm.check_winner() == BLANK:
            v.show_board(cm.get_game_string())
            v.show_pieces(cm.get_game_string())
            v.show_score(cm.black_pieces, cm.white_pieces, cm.black_move)
            cm.king_pieces()

            pos = v.get_click()
            move = self.get_move_from_pos(pos)
            b = cm.board.board

            if cm.check_move_validity(move):
                cm.make_move(move[0], move[1], move[2], move[3])

