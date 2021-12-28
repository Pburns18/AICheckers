from CheckersModel.gameConstants import WHITE, BLACK, BLANK
import copy


class Minimax:

    def minimax_value(self, model, depth, alpha, beta):

        if depth == 0:
            return self.evaluation_function(model)

        if model.black_move:
            legal_moves = model.get_all_moves(color=BLACK)
            if len(legal_moves) == 0:
                return float("inf")
        else:
            legal_moves = model.get_all_moves(color=WHITE)
            if len(legal_moves) == 0:
                return float("-inf")

        if len(legal_moves) == 0:
            return self.evaluation_function(model)

        # If it is whites turn ->
        if not model.black_move:
            value = alpha
            moves = model.get_all_moves(WHITE)
            sorted_states = []

            for move in moves:
                cm = copy.deepcopy(model)
                cm.make_move(row_from=move[0], col_from=move[1],
                             row_to=move[2], col_to=move[3])
                sorted_states.append(cm)
            sorted_states.sort(key=self.evaluation_function)

            for state in sorted_states:
                possible_value = self.minimax_value(state, depth - 1, alpha, beta)
                if possible_value > value:
                    value = possible_value
                if value > alpha:
                    alpha = value
                if beta <= alpha:
                    break
            return value

        else:
            value = beta
            moves = model.get_all_moves(BLACK)
            sorted_states = []
            for move in moves:
                cm = copy.deepcopy(model)
                cm.make_move(row_from=move[0], col_from=move[1],
                             row_to=move[2], col_to=move[3])
                sorted_states.append(cm)
            sorted_states.sort(key=self.evaluation_function)

            for state in sorted_states:
                possible_value = self.minimax_value(state, depth - 1, alpha, beta)
                if possible_value < value:
                    value = possible_value
                if value < beta:
                    beta = value
                if beta <= alpha:
                    break
            return value

    @staticmethod
    def evaluation_function(model, color=WHITE, piece_multiplier=1, king_multiplier=3, turn_multiplier=2):
        board = model.board.board
        score = 0

        if not model.black_move:
            score += turn_multiplier

        for row in board:
            for piece in row:
                if piece == BLANK:
                    continue
                if piece.color == color:
                    if piece.king:
                        score += king_multiplier
                    else:
                        score += piece_multiplier
                else:
                    if piece.king:
                        score += king_multiplier * -1
                    else:
                        score += piece_multiplier * -1

        return score
