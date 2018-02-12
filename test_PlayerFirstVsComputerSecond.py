import unittest

from PlayerFirstVsComputerSecond import PlayerFirstVsComputerSecond

class TestGame(unittest.TestCase):

    def test_complete_game_tie(self):
        player_one = "A"
        player_two = "X"

        board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = [5, 6, 1, 8, 0].pop
        self.assertTrue(PlayerFirstVsComputerSecond(player_one, player_two, board))
        __builtins__.raw_input = original_raw_input

    def test_complete_game_computerwins(self):
        player_one = "A"
        player_two = "X"

        board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = [3, 8, 0].pop
        self.assertTrue(PlayerFirstVsComputerSecond(player_one, player_two, board))
        __builtins__.raw_input = original_raw_input

if __name__ == '__main__':
    unittest.main()