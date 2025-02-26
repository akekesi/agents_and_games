from agents_and_games.utils.players import Players
from agents_and_games.utils.get_input import get_input
from agents_and_games.games.tic_tac_toe import TicTacToe
from agents_and_games.agents.agent_human import AgentHuman
from agents_and_games.agents.agent_random import AgentRandom
from agents_and_games.agents.agent_minimax import AgentMinimax
from agents_and_games.agents.agent_mcts import AgentMCTS
from agents_and_games.agents.agent_model_tic_tac_toe import AgentModelTicTacToe


class AgentExit:
    pass


def main(game_constructor):
    game = game_constructor()
    players_dict = {
        "0": AgentExit(),
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
    players_text = (", ".join(f"{key} - {player.__class__.__name__.replace("Agent", "")}" for key, player in players_dict.items()))

    while True:

        # choose the first player
        player_1 = get_input(
            message=f"Choose the first player ({players_text}): ",
            answers=answers,
        )

        # exit the game
        if player_1 == "0":
            break

        # choose the second player
        player_2 = get_input(
            message=f"Choose the second player ({players_text}): ",
            answers=answers,
        )

        # exit the game
        if player_2 == "0":
            break

        # play the game
        game.init_board()
        game.init_player()
        game.play_game(
            player_1=players_dict[player_1],
            player_2=players_dict[player_2],
        )


if __name__ == "__main__":
    GameConstructor = TicTacToe
    main(game_constructor=GameConstructor)
