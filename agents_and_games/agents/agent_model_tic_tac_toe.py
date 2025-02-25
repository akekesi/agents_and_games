import os
import numpy as np

from agents_and_games.utils.players import Players
from agents_and_games.nn.nn_tic_tac_toe import TicTacToeNN
from agents_and_games.nn.nn_tic_tac_toe import load_trained_model, get_move


class AgentModelTicTacToe:
    model = TicTacToeNN()
    suffix  ="test"
    game_name = "TicTacToe"
    agent_name = "AgentMinimax"
    name_subdir = f"{game_name}_{agent_name}_{suffix}"
    path_data_dir = os.path.join(os.path.dirname(__file__),"..", "data", name_subdir)
    path_model_pth = os.path.join(path_data_dir, "model.pth")
    map_ = Players.MAP.value

    def __init__(self):
        self.trained_model = load_trained_model(
            model=self.model,
            path_model_trained=self.path_model_pth,
        )

    def get_move(self, game, silent=False) -> tuple[int, int]:
        row = len(game.board)
        col = len(game.board[0])
        board = np.array([self.map_[game.board[r][c]] for r in range(row) for c in range(col)])

        return get_move(
            model=self.trained_model,
            board=board
        )
