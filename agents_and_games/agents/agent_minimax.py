class AgentMinimax:

    def __init__(self, players, max_depth=0):
        self.game = None
        self.players = players
        self.max_depth = max_depth

    def minimax(self, is_maximizing, depth, alpha=-float('inf'), beta=float('inf')):
        if self.game.is_winner('X'):
            return 1 / depth if depth != 0 else 1  # Prefer quicker wins
        if self.game.is_winner('O'):
            return -1 / depth if depth != 0 else -1  # Prefer slower losses
        if self.game.is_draw() or depth >= self.max_depth:
            return 0  # Stop searching if game is over or max depth is reached

        moves = self.game.get_valid_moves()
        best_score = -float('inf') if is_maximizing else float('inf')

        for move in moves:
            self.game.make_move(move=move)
            score = self.minimax(not is_maximizing, depth + 1, alpha, beta)
            self.game.undo_move(move=move)

            if is_maximizing:
                best_score = max(best_score, score)
                alpha = max(alpha, best_score)
            else:
                best_score = min(best_score, score)
                beta = min(beta, best_score)

            # Alpha-beta pruning
            if beta <= alpha:
                break

        return best_score

    def get_move(self, game, silent=False) -> tuple[int, int]:
        self.game = game
        best_move = None
        player = self.game.player
        moves = self.game.get_valid_moves()
        
        is_maximizing = player == self.players.P1.value
        best_score = -float('inf') if is_maximizing else float('inf')
        
        for move in moves:
            self.game.make_move(move=move)
            score = self.minimax(not is_maximizing, 1)
            self.game.undo_move(move=move)
            
            if (is_maximizing and score > best_score) or (not is_maximizing and score < best_score):
                best_score = score
                best_move = move
                
        return best_move
