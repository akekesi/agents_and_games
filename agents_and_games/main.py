from agents_and_games.utils.players import Players
from agents_and_games.games.tic_tac_toe import TicTacToe
from agents_and_games.agents.agent_human import AgentHuman
from agents_and_games.agents.agent_random import AgentRandom
from agents_and_games.agents.agent_minimax import AgentMinimax


def main():
    tic_tac_toe = TicTacToe()
    agent_human = AgentHuman()
    agent_random = AgentRandom()
    agent_minimax = AgentMinimax(players=Players, max_depth=5)

    # human vs human
    print()
    print("Human vs Human")
    tic_tac_toe.init_board()
    tic_tac_toe.init_player()
    tic_tac_toe.play_game(player_1=agent_human, player_2=agent_human)

    # human vs random
    print()
    print("Human vs Random")
    tic_tac_toe.init_board()
    tic_tac_toe.init_player()
    tic_tac_toe.play_game(player_1=agent_human, player_2=agent_random)

    # random vs human
    print()
    print("Random vs Human")
    tic_tac_toe.init_board()
    tic_tac_toe.init_player()
    tic_tac_toe.play_game(player_1=agent_random, player_2=agent_human)

    # random vs random
    print()
    print("Random vs Random")
    tic_tac_toe.init_board()
    tic_tac_toe.init_player()
    tic_tac_toe.play_game(player_1=agent_random, player_2=agent_random)

    # human vs minimax
    print()
    print("Human vs Minimax")
    tic_tac_toe.init_board()
    tic_tac_toe.init_player()
    tic_tac_toe.play_game(player_1=agent_human, player_2=agent_minimax)

    # minimx vs human
    print()
    print("Minimax vs Human")
    tic_tac_toe.init_board()
    tic_tac_toe.init_player()
    tic_tac_toe.play_game(player_1=agent_minimax, player_2=agent_human)


if __name__ == "__main__":
    main()
