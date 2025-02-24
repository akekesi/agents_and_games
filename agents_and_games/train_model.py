import os
import numpy as np

from agents_and_games.utils.data import load_data
from torch.utils.data import TensorDataset, DataLoader
from agents_and_games.nn.nn_tic_tac_toe import TicTacToeNN, train, load_trained_model, evaluate, get_move


if __name__ == "__main__":
    # Define paths
    suffix  ="test"
    game_name = "TicTacToe"
    agent_name = "AgentMinimax"
    name_subdir = f"{game_name}_{agent_name}_{suffix}"
    path_data_dir = os.path.join(os.path.dirname(__file__), "data", name_subdir)
    path_data_csv = os.path.join(path_data_dir, "game_data.csv")
    path_data_csv_train = path_data_csv.replace(".csv", "_train.csv")
    path_data_csv_test = path_data_csv.replace(".csv", "_test.csv")
    path_model_pth = os.path.join(path_data_dir, "model.pth")
    path_accuracy_csv = path_model_pth.replace(".pth", "_accuracy.csv")

    # Load training and test data
    X_train, y_train = load_data(path_data_csv_train)
    X_test, y_test = load_data(path_data_csv_test)

    # Initialize the model
    model = TicTacToeNN()

    # Create PyTorch DataLoader for batching
    train_dataset = TensorDataset(X_train, y_train)
    test_dataset = TensorDataset(X_test, y_test)

    train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

    # Train the model
    train(
        model=model,
        train_loader=train_loader,
        test_loader=test_loader,
        path_model_pth=path_model_pth,
        epochs=50
    )

    # Load the trained model
    model = load_trained_model(
        model=TicTacToeNN(),
        path_model_trained=path_model_pth,
    )

    # Evaluate the model
    evaluate(
        model=model,
        test_loader=test_loader,
        path_accuracy_csv=path_accuracy_csv,
    )

    # Example usage
    example_board = np.array([
        [1, -1,  0],
        [0,  1, -1],
        [0,  -1,  0]
    ])  # Example Tic-Tac-Toe state

    predicted_move = get_move(model, example_board)
    print(f"Predicted Move: {predicted_move}")

    example_board = np.array([
        [1, 0,  -1],
        [0,  0, 0],
        [1,  1,  -1]
    ])  # Example Tic-Tac-Toe state

    predicted_move = get_move(model, example_board)
    print(f"Predicted Move: {predicted_move}")

    example_board = np.array([
        [1, -1,  -1],
        [0,  0, 0],
        [1,  1,  -1]
    ])  # Example Tic-Tac-Toe state

    predicted_move = get_move(model, example_board)
    print(f"Predicted Move: {predicted_move}")
