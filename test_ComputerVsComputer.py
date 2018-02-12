import unittest

from ComputerVsComputer import ComputerVsComputer

class TestGame(unittest.TestCase):

    def test_complete_game_tie(self):
        player_one = "A"
        player_two = "X"

        board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

        tie = ComputerVsComputer(player_one, player_two, board)

        self.assertTrue(tie)

if __name__ == '__main__':
    unittest.main()