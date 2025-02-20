from agents_and_games.utils.players import Players
from agents_and_games.utils.get_input import get_input
from agents_and_games.games.tic_tac_toe import TicTacToe
from agents_and_games.agents.agent_human import AgentHuman
from agents_and_games.agents.agent_random import AgentRandom
from agents_and_games.agents.agent_minimax import AgentMinimax


def main():
    tic_tac_toe = TicTacToe()
    players = "(1 - Human, 2 - Random, 3 - Minimax)"
    players = {
        "1": AgentHuman(),
        "2": AgentRandom(),
        "3": AgentMinimax(players=Players, max_depth=5),
    }
    answers = players.keys()
    # choose the first player
    player_1 = get_input(
        message=f"Choose the first player {players}: ",
        answers=answers,
    )
    # choose the second player
    player_2 = get_input(
        message=f"Choose the second player {players}: ",
        answers=answers,
    )
    tic_tac_toe.play_game(
        player_1=players[player_1],
        player_2=players[player_2],
    )


if __name__ == "__main__":
    main()
