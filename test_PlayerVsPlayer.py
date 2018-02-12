import unittest

from PlayerVsPlayer import PlayerVsPlayer

class TestGame(unittest.TestCase):

    def test_complete_game_tie(self):
        player_one = "A"
        player_two = "X"

        board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = [7, 8, 5, 3, 6 ,2, 1, 4, 0].pop
        self.assertTrue(PlayerVsPlayer(player_one, player_two, board))
        __builtins__.raw_input = original_raw_input

    def test_complete_game_playeronewins(self):
        player_one = "A"
        player_two = "X"

        board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = [6, 4, 3, 1, 0].pop
        self.assertTrue(PlayerVsPlayer(player_one, player_two, board))
        __builtins__.raw_input = original_raw_input

    def test_complete_game_playertwowins(self):
        player_one = "A"
        player_two = "X"

        board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = [7 ,8, 4, 3, 1, 0].pop
        self.assertTrue(PlayerVsPlayer(player_one, player_two, board))
        __builtins__.raw_input = original_raw_input

if __name__ == '__main__':
    unittest.main()