import unittest

from EndGameConditions import EndGameConditions

class EndGameTest(unittest.TestCase):

    # Testing multiple game over conditions

    def test_game_over_one(self):
        board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
        game_end = EndGameConditions().game_is_over("X", "O", board)
        self.assertFalse(game_end)

    def test_game_over_two(self):
        board = ["X", "X", "X", "3", "4", "5", "6", "7", "8"]
        game_end = EndGameConditions().game_is_over("X", "O", board)
        self.assertTrue(game_end)

    def test_game_over_three(self):
        board = ["0", "1", "2", "O", "O", "O", "6", "7", "8"]
        game_end = EndGameConditions().game_is_over("X", "O", board)
        self.assertTrue(game_end)

    def test_game_over_four(self):
        board = ["0", "1", "2", "3", "4", "5", "X", "X", "X"]
        game_end = EndGameConditions().game_is_over("X", "O", board)
        self.assertTrue(game_end)

    def test_game_over_five(self):
        board = ["O", "1", "2", "O", "4", "5", "O", "7", "8"]
        game_end = EndGameConditions().game_is_over("X", "O", board)
        self.assertTrue(game_end)

    def test_game_over_six(self):
        board = ["0", "X", "2", "3", "X", "5", "6", "X", "8"]
        game_end = EndGameConditions().game_is_over("X", "O", board)
        self.assertTrue(game_end)

    def test_game_over_seven(self):
        board = ["0", "1", "O", "3", "4", "O", "6", "7", "O"]
        game_end = EndGameConditions().game_is_over("X", "O", board)
        self.assertTrue(game_end)

    def test_game_over_eight(self):
        board = ["X", "1", "2", "3", "X", "5", "6", "7", "X"]
        game_end = EndGameConditions().game_is_over("X", "O", board)
        self.assertTrue(game_end)

    def test_game_over_nine(self):
        board = ["0", "1", "X", "3", "X", "5", "X", "7", "8"]
        game_end = EndGameConditions().game_is_over("X", "O", board)
        self.assertTrue(game_end)

if __name__ == '__main__':
    unittest.main()



