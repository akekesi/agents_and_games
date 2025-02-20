import random


class AgentRandom:
    @staticmethod
    def get_move(game) -> tuple[int, int]:
        move = random.choice(game.get_valid_moves())
        print(f"Player-{game.player}: {move[0]} {move[1]}")
        return move
