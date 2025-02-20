class AgentHuman:
    @staticmethod
    def get_move(game) -> tuple[int, int]:
        move = None
        while move is None:
            try:
                move = tuple(map(int, input(f"Player-{game.player}: ").split()))
                if len(move) != 2:
                    raise ValueError
                if not game.is_valid_move(move=move):
                    print("Invalid move. Try again.")
                    move = None
            except ValueError:
                print("Invalid input. Try again.")
                move = None
        return move
