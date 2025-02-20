from agents_and_games.utils.players import Players
from agents_and_games.utils.get_input import get_input
from agents_and_games.games.tic_tac_toe import TicTacToe
from agents_and_games.agents.agent_human import AgentHuman
from agents_and_games.agents.agent_random import AgentRandom
from agents_and_games.agents.agent_minimax import AgentMinimax


def main():
    game = TicTacToe()
    players_dict = {
        "1": AgentHuman(),
        "2": AgentRandom(),
        "3": AgentMinimax(players=Players, max_depth=5),
    }
    answers = players_dict.keys()
    players_text = (", ".join(f"{key} - {player.__class__.__name__.replace("Agent", "")}" for key, player in players_dict.items()))

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

    # play the game
    game.play_game(
        player_1=players_dict[player_1],
        player_2=players_dict[player_2],
    )


if __name__ == "__main__":
    main()
