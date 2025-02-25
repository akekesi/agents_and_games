from agents_and_games.utils.plot import plot_losses
from agents_and_games.utils.globals import PATH_MODEL_LOSSES_CSV


if __name__ == "__main__":
    # Number of samples
    n_samples = 5400

    # Plot losses
    plot_losses(
        path_losses_csv=PATH_MODEL_LOSSES_CSV,
        n_samples=n_samples,
    )
