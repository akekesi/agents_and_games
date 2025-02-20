class AgentMinimax:

    def __init__(self, players, max_depth=0):
        self.game = None
        self.players = players
        self.max_depth = max_depth

    def minimax(self, is_maximizing, depth):
        if self.game.is_winner('X'):
            return 1 / depth if depth != 0 else 1  # Prefer quicker wins
        if self.game.is_winner('O'):
            return -1 / depth if depth != 0 else -1  # Prefer slower losses
        if self.game.is_draw() or depth >= self.max_depth:
            return 0  # Stop searching if game is over or max depth is reached

        moves = self.game.get_valid_moves()
        if is_maximizing:
            max_score = -float("inf")
            for move in moves:
                self.game.make_move(move=move)
                max_score = max(max_score, self.minimax(is_maximizing=False, depth=depth + 1))
                self.game.undo_move(move=move)
            return max_score
        else:
            min_score = float("inf")
            for move in moves:
                self.game.make_move(move=move)
                min_score = min(min_score, self.minimax(is_maximizing=True, depth=depth + 1))
                self.game.undo_move(move=move)
            return min_score

    def get_move(self, game):
        self.game = game
        move_best = None
        player = self.game.player
        moves = self.game.get_valid_moves()
        if player == self.players.P1.value:
            score_best = -float("inf")
            for move in moves:
                self.game.make_move(move=move)
                score = self.minimax(is_maximizing=False, depth=1)
                self.game.undo_move(move=move)
                if score > score_best:
                    score_best = score
                    move_best = move
        if player == self.players.P2.value:
            score_best = float("inf")
            for move in moves:
                self.game.make_move(move=move)
                score = self.minimax(is_maximizing=True, depth=1)
                self.game.undo_move(move=move)
                if score < score_best:
                    score_best = score
                    move_best = move
        return move_best
