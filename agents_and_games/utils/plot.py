import pandas as pd

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def plot_losses(path_losses_csv, n_samples):
    """Plot the training and validation losses."""
    df = pd.read_csv(path_losses_csv)
    plt.plot(df["epoch"], df["avg_train_loss"], label="avg_train_loss")
    plt.plot(df["epoch"], df["avg_val_loss"], label="avg_val_loss")
    plt.title(f"Training & Validation Loss ({n_samples} samples)")
    plt.ylabel("Loss")
    plt.xlabel("Epoch")
    plt.legend()
    plt.grid()
    path_losses_png = path_losses_csv.replace(".csv", ".png")
    plt.savefig(path_losses_png)
    plt.close()
