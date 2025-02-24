import os
import time

from datetime import timedelta
from agents_and_games.utils.players import Players
from agents_and_games.games.tic_tac_toe import TicTacToe
from agents_and_games.agents.agent_minimax import AgentMinimax
from agents_and_games.agents.agent_mcts import AgentMCTS
from agents_and_games.utils.data import get_data, data_to_csv, split_csv, load_data


if __name__ == "__main__":
    # Initialize the game
    game = TicTacToe()

    # Initialize the agent
    agent = AgentMinimax(
        players=Players,
        max_depth=999,
    )
    # agent = AgentMCTS(
    #     game_constructor=TicTacToe,
    #     players=Players,
    #     max_depth=999,
    #     iterations=1000,
    # )

    # Define the paths and mapping
    suffix  ="test"
    name_subdir = f"{game.__class__.__name__}_{agent.__class__.__name__}_{suffix}"
    path_data_dir = os.path.join(os.path.dirname(__file__), "data", name_subdir)
    path_data_csv = os.path.join(path_data_dir, "game_data.csv")
    map_ = Players.MAP.value

    # Create the directory if it does not exist
    os.makedirs(path_data_dir, exist_ok=True)

    # Start the timer
    start_time = time.time()

    # Get the data
    df = get_data(
        game=game,
        agent=agent,
        map_=map_,
    )

    # Save the data to a CSV file
    data_to_csv(
        df=df,
        path_data_csv=path_data_csv,
    )

    # Stop the timer
    end_time = time.time()

    # Print the execution time and some information about the game, agent, and data
    execution_time = timedelta(seconds=end_time - start_time)
    print(f"{execution_time = }")
    print(f"{game.__class__.__name__ = }")
    print(f"{agent.__class__.__name__ = }")

    # Display the first few rows of the data
    print(f"{df.shape = }")
    print(f"{df.head() = }")

    # Split the data into train and test sets
    path_data_train_csv, path_data_test_csv = split_csv(
        path_csv=path_data_csv,
        test_size=0.2,
        random_state=42,
    )

    # Display the paths to the training and testing datasets
    print(f"{path_data_csv = }")
    print(f"{path_data_train_csv = }")
    print(f"{path_data_test_csv = }")

    # Load the training datasets
    train_boards, train_moves = load_data(path_csv=path_data_train_csv)

    # Display the shapes and first few elements of the training datasets
    print("Training Data")
    print(f"{train_boards.shape = }")
    print(f"{train_moves.shape = }")
    print(f"{train_boards[0] = }")
    print(f"{train_moves[0] = }")

    # Load testing datasets
    test_boards, test_moves = load_data(path_csv=path_data_test_csv)

    # Display the shapes and first few elements of the testing datasets
    print("Testing Data")
    print(f"{test_boards.shape = }")
    print(f"{test_moves.shape = }")
    print(f"{test_boards[0] = }")
    print(f"{test_moves[0] = }")
