import numpy as np
import pandas as pd

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def plot_losses(path_losses_csv, n_samples):
    """Plot the training and validation losses."""
    df = pd.read_csv(path_losses_csv)

    _, ax1 = plt.subplots()

    # Create a first y-axis
    line_1, = ax1.plot(df["epoch"], df["avg_train_loss"], "b-", label="avg_train_loss")
    line_2, = ax1.plot(df["epoch"], df["avg_val_loss"], "r-", label="avg_val_loss")
    ax1.set_xlabel("Epoch")
    ax1.set_ylabel("Avg. Loss")
    ax1.grid(True, which='both', linestyle='--', linewidth=0.5)

    # Create a second y-axis
    ax2 = ax1.twinx()
    line_3, = ax2.plot(df["epoch"], df["accuracy"]*100, "g-",label="accuracy")
    ax2.set_ylabel("Accuracy [%]")
    ax2.grid(False)

    # Set y-axis ticks
    num_ticks = 6
    y1_min, y1_max = ax1.get_ylim()
    y2_min, y2_max = 0, 100  # Accuracy is between 0 and 100 percent

    y1_min = np.floor(y1_min * 10) / 10
    y1_max = (np.ceil(((np.ceil(y1_max * 10) / 10 - y1_min) / (num_ticks - 1)) * 10) / 10) * (num_ticks - 1)

    y1_ticks = np.linspace(y1_min, y1_max, num_ticks)
    y2_ticks = np.linspace(y2_min, y2_max, num_ticks)

    ax1.set_yticks(y1_ticks)
    ax2.set_yticks(y2_ticks)

    # Set legends
    lines = [line_1, line_2, line_3]
    labels = [line.get_label() for line in lines]
    ax1.legend(lines, labels, loc="center right")

    # Set title
    plt.title(f"Avg. Loss & Accuracy\n({n_samples} samples, train - test: 80% - 20%)")

    # Save the plot
    path_losses_png = path_losses_csv.replace(".csv", ".png")
    plt.tight_layout()
    plt.savefig(path_losses_png)

    # Close the plot
    plt.close()
