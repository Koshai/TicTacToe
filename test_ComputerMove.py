import unittest

from ComputerMove import ComputerMove

class TestMoves(unittest.TestCase):

    # Testing different computer move based on different board scenarios
    def test_makemove_one(self):
        computer = "X"
        opponent = "Y"
        board = ["0", "1", "2", "3", "Y", "5", "6", "7", "8"]

        expected = computer, "0"
        result = ComputerMove().eval_board(computer, opponent, board)

        self.assertEqual(expected, result)

    def test_makemove_two(self):
        computer = "X"
        opponent = "Y"
        board = ["Y", "1", "2", "3", "4", "5", "6", "7", "8"]

        expected = computer, "4"
        result = ComputerMove().eval_board(computer, opponent, board)

        self.assertEqual(expected, result)

    def test_makemove_three(self):
        computer = "X"
        opponent = "Y"
        board = ["Y", "Y", "2", "3", "X", "5", "6", "7", "8"]

        expected = computer, "2"
        result = ComputerMove().eval_board(computer, opponent, board)

        self.assertEqual(expected, result)

    def test_makemove_three(self):
        computer = "X"
        opponent = "Y"
        board = ["Y", "1", "2", "Y", "X", "5", "6", "7", "8"]

        expected = computer, "6"
        result = ComputerMove().eval_board(computer, opponent, board)

        self.assertEqual(expected, result)

    def test_makemove_four(self):
        computer = "X"
        opponent = "Y"
        board = ["Y", "Y", "2", "3", "X", "5", "6", "7", "8"]

        expected = computer, "2"
        result = ComputerMove().eval_board(computer, opponent, board)

        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()