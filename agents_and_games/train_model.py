import numpy as np

from agents_and_games.utils.data import load_data
from torch.utils.data import TensorDataset, DataLoader
from agents_and_games.nn.nn_tic_tac_toe import TicTacToeNN, train, load_trained_model, get_move
from agents_and_games.utils.globals import PATH_DATA_CSV, PATH_MODEL_PTH, PATH_DATA_CSV_TRAIN, PATH_DATA_CSV_TEST, PATH_MODEL_ACCURACY_CSV


if __name__ == "__main__":
    # Load training and test data
    X_train, y_train = load_data(PATH_DATA_CSV_TRAIN)
    X_test, y_test = load_data(PATH_DATA_CSV_TEST)

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
        path_model_pth=PATH_MODEL_PTH,
        epochs=50
    )

    # Load the trained model
    model = load_trained_model(
        model=TicTacToeNN(),
        path_model_trained=PATH_MODEL_PTH,
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
