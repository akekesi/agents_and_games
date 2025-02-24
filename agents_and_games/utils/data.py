import torch
import itertools
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split

from agents_and_games.utils.players import Players


def is_valid_board(board, players, is_winner):
    # Count the number of P1-tokens and P2-tokens
    p1_count = np.sum(board == players.P1.value)
    p2_count = np.sum(board == players.P2.value)

    # Check if P1 or P2 has won
    p1_wins = is_winner(player=players.P1.value, board=board)
    p2_wins = is_winner(player=players.P2.value, board=board)

    # P1 always moves first, so there should be either the same number of P1-tokens and P2-tokens or one more P1-token than P2-token
    if p1_count != p2_count and p1_count != p2_count + 1:
        return False

    # Both players cannot win at the same time
    if p1_wins and p2_wins:
        return False

    # If P1 has won, there should be exactly one more P1-token than P2-token
    if p1_wins and p1_count != p2_count + 1:
        return False

    # If P2 has won, there should be an equal number of P1-tokens and P2-tokens
    if p2_wins and p1_count != p2_count:
        return False

    return True


def generate_valid_boards(row, col, players, is_winner):
    # Initialize the set of valid boards
    valid_boards = set()
    tokens = [player.value for player in players if isinstance(player.value, str)]

    # Iterate through all possible board configurations
    for state in itertools.product(tokens, repeat=row * col):
        board = np.array(state).reshape(row, col)

        # Check if the board is valid
        if is_valid_board(
            board=board,
            players=players,
            is_winner=is_winner,
        ):
            valid_boards.add(tuple(board.flatten()))

    return [np.array(valid_board).reshape(row, col).tolist() for valid_board in valid_boards]


def get_data(game, agent, map_):
    # Get the number of rows and columns in the game board
    row = len(game.board)
    col = len(game.board[0])

    # Generate all valid boards
    valid_boards = generate_valid_boards(
        row=row,
        col=col,
        players=agent.players,
        is_winner=game.is_winner,
    )

    # Get the move for each valid board and store the data
    data  =[]
    columns = [f"r{r}_c{c}" for r in range(row) for c in range(col)] + ["move_r", "move_c"]
    for valid_board in valid_boards:
        game.board = valid_board
        game.player = Players.P1.value if np.sum(valid_board == Players.EMPTY.value) % 2 else Players.P2.value
        move = agent.get_move(game=game)
        if move is not None: # If the game is over, there is no move
            data.append([map_[valid_board[r][c]] for r in range(row) for c in range(col)] + [move[0], move[1]])

    # Create a DataFrame
    df = pd.DataFrame(data, columns=columns)

    return df


def data_to_csv(df, path_data_csv):
    df.to_csv(path_data_csv, index=False)


def split_csv(
    path_csv: str,
    test_size: float,
    random_state: int,
) -> tuple:
    # Load the dataset
    df = pd.read_csv(path_csv)

    # Split into train and test sets
    train, test = train_test_split(df, test_size=test_size, random_state=random_state)

    # Generate output file names
    path_csv_train = path_csv.replace(".csv", "_train.csv")
    path_csv_test = path_csv.replace(".csv", "_test.csv")

    # Save to CSV files
    train.to_csv(path_csv_train, index=False)
    test.to_csv(path_csv_test, index=False)

    return path_csv_train, path_csv_test


def load_data(path_csv):
    # Load the dataset
    df = pd.read_csv(path_csv)

    # Extract the boards and moves
    boards = df.iloc[:, :-2].astype(int).values.tolist()
    moves = df.iloc[:, -2:].astype(int).values.tolist()

    # Convert to NumPy arrays
    boards = np.array(boards)
    moves = np.array([move[0] * 3 + move[1] for move in moves])

    # Convert to PyTorch tensors
    return torch.tensor(boards, dtype=torch.float32), torch.tensor(moves, dtype=torch.long)
