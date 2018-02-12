import unittest

from Tie import Tie

class EndGameTest(unittest.TestCase):

    def test_game_over_one(self):
        board = ["O", "X", "O", "X", "X", "O", "X", "O", "X"]
        tie = Tie().tie("X", "O", board)
        self.assertTrue(tie)

    def test_game_over_two(self):
        board = ["X", "1", "2", "3", "O", "5", "6", "7", "8"]
        tie = Tie().tie("X", "O", board)
        self.assertFalse(tie)

if __name__ == '__main__':
    unittest.main()



