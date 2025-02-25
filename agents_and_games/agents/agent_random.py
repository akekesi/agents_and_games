import random


class AgentRandom:
    @staticmethod
    def get_move(game, silent=False) -> tuple[int, int]:
        move = random.choice(game.get_valid_moves())
        if not silent:
            print(f"Player-{game.player}: {move[0]} {move[1]}")
        return move
