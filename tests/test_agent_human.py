import unittest
from unittest.mock import patch
from agents_and_games.games.tic_tac_toe import TicTacToe
from agents_and_games.agents.agent_human import AgentHuman


class TestAgentHuman(unittest.TestCase):

    def setUp(self):
        self.tic_tac_toe = TicTacToe()
        self.agent_human = AgentHuman()

    def tearDown(self):
        del self.tic_tac_toe
        del self.agent_human

    @patch("builtins.input", side_effect=["", "abc-123", "1, 2", "1 1 1", "-1 2", "0 3", "1 2"])
    def test_get_move_01(self, mock_input):
        self.assertEqual(self.agent_human.get_move(game=self.tic_tac_toe), (1, 2))
        self.assertEqual(mock_input.call_count, 7)

    @patch("builtins.input", side_effect=["", "abc-123", "1, 2", "1 1 1", "-1 2", "0 3", "1 2"])
    def test_get_move_02(self, mock_input):
        self.assertEqual(AgentHuman.get_move(game=self.tic_tac_toe), (1, 2))
        self.assertEqual(mock_input.call_count, 7)


if __name__ == "__main__":
    unittest.main()
