import unittest
from agents_and_games.games.tic_tac_toe import TicTacToe


class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        self.tic_tac_toe = TicTacToe()

    def tearDown(self):
        del self.tic_tac_toe

    def test_init_board(self):
        board_expected = [[" " for _ in range(3)] for _ in range(3)]

        self.assertEqual(self.tic_tac_toe.board, board_expected)

        self.tic_tac_toe.board[0][0] = "X"
        self.tic_tac_toe.init_board()
        self.assertEqual(self.tic_tac_toe.board, board_expected)

        self.tic_tac_toe.board[0][0] = "X"
        self.tic_tac_toe.board[0][2] = "O"
        self.tic_tac_toe.board[1][1] = "X"
        self.tic_tac_toe.board[1][2] = "O"
        self.tic_tac_toe.board[2][2] = "X"
        self.tic_tac_toe.init_board()
        self.assertEqual(self.tic_tac_toe.board, board_expected)

    def test_init_player(self):
        self.assertEqual(self.tic_tac_toe.player, "X")

        self.tic_tac_toe.init_player(player="O")
        self.assertEqual(self.tic_tac_toe.player, "O")

        self.tic_tac_toe.init_player(player="X")
        self.assertEqual(self.tic_tac_toe.player, "X")

    def test_switch_player(self):
        self.assertEqual(self.tic_tac_toe.player, "X")

        self.tic_tac_toe.switch_player()
        self.assertEqual(self.tic_tac_toe.player, "O")

        self.tic_tac_toe.switch_player()
        self.assertEqual(self.tic_tac_toe.player, "X")

    def test_make_move(self):
        moves = [
            (0, 0),
            (1, 2),
            (2, 0),
        ]
        players = [
            "X",
            "O",
            "X",
        ]
        for move, player in zip(moves, players):
            self.assertEqual(self.tic_tac_toe.player, player)
            self.tic_tac_toe.make_move(move=move)
            self.assertEqual(self.tic_tac_toe.board[move[0]][move[1]], player)

    def test_undo_move(self):
        moves = [
            (0, 0),
            (1, 2),
            (2, 0),
        ]
        for move in moves:
            self.tic_tac_toe.make_move(move=move)
            self.assertEqual(self.tic_tac_toe.player, "O")
            self.assertEqual(self.tic_tac_toe.board[move[0]][move[1]], "X")
            self.tic_tac_toe.undo_move(move=move)
            self.assertEqual(self.tic_tac_toe.player, "X")
            self.assertEqual(self.tic_tac_toe.board[move[0]][move[1]], " ")
            self.assertEqual(self.tic_tac_toe.board[move[0]][move[1]], " ")

    def test_is_valid_move(self):
        self.assertTrue(self.tic_tac_toe.is_valid_move(move=(0, 0)))
        self.assertTrue(self.tic_tac_toe.is_valid_move(move=(1, 2)))
        self.assertTrue(self.tic_tac_toe.is_valid_move(move=(2, 0)))

        self.tic_tac_toe.board = [
            ["X", "X", " "],
            ["O", "O", "X"],
            ["X", " ", "O"],
        ]
        self.assertTrue(self.tic_tac_toe.is_valid_move(move=(0, 2)))
        self.assertTrue(self.tic_tac_toe.is_valid_move(move=(2, 1)))
        self.assertFalse(self.tic_tac_toe.is_valid_move(move=(0, 0)))
        self.assertFalse(self.tic_tac_toe.is_valid_move(move=(1, 2)))
        self.assertFalse(self.tic_tac_toe.is_valid_move(move=(2, 0)))

    def test_is_winner(self):
        self.tic_tac_toe.board = [
            ["X", "X", "X"],
            ["O", "O", " "],
            [" ", "O", " "],
        ]
        self.assertTrue(self.tic_tac_toe.is_winner(player="X"))
        self.assertFalse(self.tic_tac_toe.is_winner(player="O"))

        self.tic_tac_toe.board = [
            ["X", "O", "X"],
            ["O", "O", " "],
            ["X", "O", "X"],
        ]
        self.assertTrue(self.tic_tac_toe.is_winner(player="O"))
        self.assertFalse(self.tic_tac_toe.is_winner(player="X"))

        self.tic_tac_toe.board = [
            ["X", "O", " "],
            ["O", "X", "O"],
            ["X", "O", "X"],
        ]
        self.assertTrue(self.tic_tac_toe.is_winner(player="X"))
        self.assertFalse(self.tic_tac_toe.is_winner(player="O"))

        self.tic_tac_toe.board = [
            ["X", "X", "O"],
            ["O", "O", "X"],
            ["O", "O", "X"],
        ]
        self.assertTrue(self.tic_tac_toe.is_winner(player="O"))
        self.assertFalse(self.tic_tac_toe.is_winner(player="X"))

        self.tic_tac_toe.board = [
            ["X", "X", "X"],
            ["O", "O", "O"],
            ["X", "O", "X"],
        ]
        self.assertTrue(self.tic_tac_toe.is_winner(player="O"))
        self.assertTrue(self.tic_tac_toe.is_winner(player="X"))

    def test_is_draw(self):
        self.tic_tac_toe.board = [
            ["X", "O", "X"],
            ["O", "O", "X"],
            ["X", "X", "O"],
        ]
        self.assertTrue(self.tic_tac_toe.is_draw())

        self.tic_tac_toe.board = [
            ["X", "X", "X"],
            ["O", "O", "X"],
            ["X", "O", "O"],
        ]
        self.assertTrue(self.tic_tac_toe.is_draw())

        self.tic_tac_toe.board = [
            ["O", "O", "O"],
            ["O", "O", "O"],
            ["O", "O", "O"],
        ]
        self.assertTrue(self.tic_tac_toe.is_draw())

        self.tic_tac_toe.board = [
            ["X", " ", "X"],
            ["O", "O", "X"],
            ["X", "X", "O"],
        ]
        self.assertFalse(self.tic_tac_toe.is_draw())


    def test_is_game_over(self):
        self.assertFalse(self.tic_tac_toe.is_game_over())

        self.tic_tac_toe.board = [
            ["X", "X", "O"],
            ["O", "X", " "],
            ["X", "O", "O"],
        ]
        self.assertFalse(self.tic_tac_toe.is_game_over())

        self.tic_tac_toe.board = [
            ["X", "X", "X"],
            ["O", "O", " "],
            [" ", "O", " "],
        ]
        self.assertTrue(self.tic_tac_toe.is_game_over())

        self.tic_tac_toe.board = [
            ["X", "X", "O"],
            ["X", "O", "O"],
            [" ", "X", "O"],
        ]
        self.assertTrue(self.tic_tac_toe.is_game_over())

        self.tic_tac_toe.board = [
            ["X", "X", "O"],
            ["O", "X", "X"],
            ["X", "O", "O"],
        ]
        self.assertTrue(self.tic_tac_toe.is_game_over())

    def test_get_valid_moves(self):
        self.assertEqual(self.tic_tac_toe.get_valid_moves(), [
            (0, 0), (0, 1), (0, 2),
            (1, 0), (1, 1), (1, 2),
            (2, 0), (2, 1), (2, 2),
        ])

        self.tic_tac_toe.board = [
            ["X", "X", " "],
            ["O", "O", " "],
            ["X", " ", "O"],
        ]
        self.assertEqual(self.tic_tac_toe.get_valid_moves(), [(0, 2), (1, 2), (2, 1)])

        self.tic_tac_toe.board = [
            ["X", " ", "X"],
            ["O", "O", "X"],
            [" ", "X", "O"],
        ]
        self.assertEqual(self.tic_tac_toe.get_valid_moves(), [(0, 1), (2, 0)])

        self.tic_tac_toe.board = [
            ["X", "O", "X"],
            [" ", "O", "X"],
            ["O", "X", "O"],
        ]
        self.assertEqual(self.tic_tac_toe.get_valid_moves(), [(1, 0)])

        self.tic_tac_toe.board = [
            ["X", "O", "X"],
            ["O", "O", "X"],
            ["X", "X", "O"],
        ]
        self.assertEqual(self.tic_tac_toe.get_valid_moves(), [])

        self.tic_tac_toe.board = [
            ["O", "O", "O"],
            ["O", "O", "O"],
            ["O", "O", "O"],
        ]
        self.assertEqual(self.tic_tac_toe.get_valid_moves(), [])


if __name__ == "__main__":
    unittest.main()
