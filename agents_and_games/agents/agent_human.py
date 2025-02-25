class AgentHuman:
    @staticmethod
    def get_move(game, silent=False) -> tuple[int, int]:
        move = None
        while move is None:
            try:
                if not silent:
                    move = tuple(map(int, input(f"Player-{game.player}: ").split()))
                else:
                    # In silent mode, this should never be called for human agent
                    raise RuntimeError("Human agent cannot be used in silent mode")
                if len(move) != 2:
                    raise ValueError
                if not game.is_valid_move(move=move):
                    print("Invalid move. Try again.")
                    move = None
            except ValueError:
                print("Invalid input. Try again.")
                move = None
        return move
