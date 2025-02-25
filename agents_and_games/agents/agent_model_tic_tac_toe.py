import numpy as np

from agents_and_games.utils.players import Players
from agents_and_games.nn.nn_tic_tac_toe import TicTacToeNN
from agents_and_games.nn.nn_tic_tac_toe import load_trained_model, get_move
from agents_and_games.utils.globals import PATH_MODEL_PTH


class AgentModelTicTacToe:
    model = TicTacToeNN()
    map_ = Players.MAP.value

    def __init__(self):
        self.trained_model = load_trained_model(
            model=self.model,
            path_model_trained=PATH_MODEL_PTH,
        )

    def get_move(self, game):
        row = len(game.board)
        col = len(game.board[0])
        board = np.array([self.map_[game.board[r][c]] for r in range(row) for c in range(col)])

        return get_move(
            model=self.trained_model,
            board=board
        )
