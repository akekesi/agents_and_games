import unittest
from unittest.mock import patch
from agents_and_games.utils.get_input import get_input


class TestGetInput(unittest.TestCase):

    @patch("builtins.input", side_effect=["x", "", "a"])
    def test_get_input_01(self, mock_input):
        message = "test_message"
        answers = ["a", "b"]
        answer = get_input(
            message=message,
            answers=answers,
        )
        self.assertEqual(answer, "a")
        self.assertEqual(mock_input.call_count, 3)

    @patch("builtins.input", side_effect=["x", "", "a"])
    def test_get_input_02(self, mock_input):
        message = "test_message"
        answers = ["a", "b"]
        message_error = "test_message_error"
        answer = get_input(
            message=message,
            answers=answers,
            message_error=message_error,
        )
        self.assertEqual(answer, "a")
        self.assertEqual(mock_input.call_count, 3)


if __name__ == "__main__":
    unittest.main()
