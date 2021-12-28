from CheckersModel.gameConstants import WHITE, BLACK, BLANK
import copy


class Minimax:

    # I think that we are crashing because in scenarios where the game is simulated out
    # and the AI or black looses - then there are technically no moves left.
    # We need to set the value of this board to either inf or -inf
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


"""
class Minimax:

    def __init__(self, model, depth, alpha=float("-inf"), beta=float("-inf"), turn=WHITE):
        self.model = model
        self.depth = depth
        self.alpha = alpha
        self.beta = beta
        self.turn = turn

    def evaluation_function(self, piece_multiplier=1, king_multiplier=3, turn_multiplier=2):
        piece_multiplier = 1
        king_multiplier = 3
        turn_multiplier = 2
        board = self.model.board.board
        score = 0

        if self.turn == WHITE:
            if not self.model.black_move:
                score += turn_multiplier

        for row in board:
            for piece in row:
                if piece == BLANK:
                    continue
                if piece.color == self.turn:
                    if piece.king:
                        score += king_multiplier
                    else:
                        score += piece_multiplier
                else:
                    if piece.king:
                        score += int(king_multiplier * -1)
                    else:
                        score += int(piece_multiplier * -1)

        return score

    def minimax_value(self):
        # If we have reached our search depth - evaluate the board
        if self.depth == 0:
            return self.evaluation_function()

        # If we have no legal moves - return our evaluation function

        # Here we are assuming that white is max and black is min
        if self.turn == WHITE:
            value = self.alpha
            # Get all legal moves for white
            moves = self.model.get_all_moves(WHITE)

            sorted_states = []
            for move in moves:
                cm = copy.deepcopy(self.model)
                cm.make_move(row_from=move[0], col_from=move[1],
                             row_to=move[2], col_to=move[3])
                sorted_states.append(cm)

            sorted_states.sort(key=self.evaluation_function)

            for state in sorted_states:
                print('Board')
                print(state.board.board)
                st = copy.deepcopy(state)
                if self.model.black_move:
                    turn = BLACK
                else:
                    turn = WHITE
                minimax = Minimax(st, self.depth - 1, self.alpha, self.beta, turn)
                possible_value = minimax.minimax_value()
                print(possible_value)

                if possible_value > value:
                    value = possible_value
                if value > self.alpha:
                    self.alpha = value
                if self.beta <= self.alpha:
                    break

            return value

        else:
            value = self.beta
            # Get all legal moves for white
            moves = self.model.get_all_moves(BLACK)

            sorted_states = []
            for move in moves:
                cm = copy.deepcopy(self.model)
                cm.make_move(row_from=move[0], col_from=move[1],
                             row_to=move[2], col_to=move[3])
                sorted_states.append(cm)

            sorted_states.sort(key=self.evaluation_function)

            for state in sorted_states:
                print('Board')
                print(state.board.board)
                if self.model.black_move:
                    turn = BLACK
                else:
                    turn = WHITE
                minimax = Minimax(state, self.depth - 1, self.alpha, self.beta, turn)
                possible_value = minimax.minimax_value()

                if possible_value < value:
                    value = possible_value
                if value < self.beta:
                    self.beta = value
                if self.beta <= self.alpha:
                    break
            return value
            """
