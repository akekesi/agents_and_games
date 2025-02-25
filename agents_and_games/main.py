from agents_and_games.utils.players import Players
from agents_and_games.utils.get_input import get_input
from agents_and_games.games.tic_tac_toe import TicTacToe
from agents_and_games.agents.agent_human import AgentHuman
from agents_and_games.agents.agent_random import AgentRandom
from agents_and_games.agents.agent_minimax import AgentMinimax
from agents_and_games.agents.agent_mcts import AgentMCTS
from agents_and_games.agents.agent_model_tic_tac_toe import AgentModelTicTacToe


def main(game_constructor):
    game = game_constructor()
    players_dict = {
        "1": AgentHuman(),
        "2": AgentRandom(),
        "3": AgentMinimax(
            players=Players,
            max_depth=999,
        ),
        "4": AgentMCTS(
            game_constructor=game_constructor,
            players=Players,
            max_depth=999,
            iterations=1000,
        ),
        "5": AgentModelTicTacToe(),
    }
    answers = players_dict.keys()
    players_text = (", ".join(f"{key} - {player.__class__.__name__.replace('Agent', '')}" for key, player in players_dict.items()))

    # choose mode
    mode = get_input(
        message="Choose mode (1 - Single Game, 2 - Batch Mode): ",
        answers=["1", "2"]
    )

    # choose the first player
    player_1 = get_input(
        message=f"Choose the first player ({players_text}): ",
        answers=answers,
    )

    # choose the second player
    player_2 = get_input(
        message=f"Choose the second player ({players_text}): ",
        answers=answers,
    )

    if mode == "1":
        # play single game
        game.play_game(
            player_1=players_dict[player_1],
            player_2=players_dict[player_2],
        )
    else:
        # batch mode
        while True:
            try:
                n_games = int(input("Enter number of games to play: "))
                if n_games > 0:
                    break
                print("Please enter a positive number")
            except ValueError:
                print("Please enter a valid number")
        
        stats = run_multiple_games(
            game_constructor=game_constructor,
            player_1=players_dict[player_1],
            player_2=players_dict[player_2],
            n_games=n_games
        )
        
        print(f"\nResults after {n_games} games:")
        print(f"Player 1 ({players_dict[player_1].__class__.__name__}) wins: {stats['player_1_wins']} ({stats['player_1_wins']/n_games*100:.1f}%)")
        print(f"Player 2 ({players_dict[player_2].__class__.__name__}) wins: {stats['player_2_wins']} ({stats['player_2_wins']/n_games*100:.1f}%)")
        print(f"Draws: {stats['draws']} ({stats['draws']/n_games*100:.1f}%)")


def run_multiple_games(game_constructor, player_1, player_2, n_games=100):
    """Run multiple games between two players and return statistics.
    
    Args:
        game_constructor: Game class constructor
        player_1: First player agent
        player_2: Second player agent
        n_games: Number of games to play
    
    Returns:
        dict: Statistics of games played
    """
    stats = {"player_1_wins": 0, "player_2_wins": 0, "draws": 0}
    
    for game_num in range(n_games):
        game = game_constructor()
        result = game.play_game(player_1=player_1, player_2=player_2, silent=True)
        
        if result == Players.P1.value:
            print("Winner: Player 1", end="\t")
            stats["player_1_wins"] += 1
        elif result == Players.P2.value:
            print("Winner: Player 2", end="\t")
            stats["player_2_wins"] += 1
        else:
            print("Winner: Draw", end="\t\t")
            stats["draws"] += 1

        print(game.board[0][0], game.board[0][1], game.board[0][2], game.board[1][0], game.board[1][1], game.board[1][2], game.board[2][0], game.board[2][1], game.board[2][2])
    
    return stats


if __name__ == "__main__":
    GameConstructor = TicTacToe
    main(game_constructor=GameConstructor)
