import os
from agents_and_games.utils.plot import plot_losses


if __name__ == "__main__":
    # Define paths
    n_samples = 5400
    suffix  ="test"
    game_name = "TicTacToe"
    agent_name = "AgentMinimax"
    name_subdir = f"{game_name}_{agent_name}_{suffix}"
    path_data_dir = os.path.join(os.path.dirname(__file__), "data", name_subdir)
    path_model_losses_csv = os.path.join(path_data_dir, "model_losses.csv")

    # Plot losses
    plot_losses(
        path_losses_csv=path_model_losses_csv,
        n_samples=n_samples,
    )
