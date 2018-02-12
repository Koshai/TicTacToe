import unittest

from Board import Board

class TestBoard(unittest.TestCase):

    def test_show_board(self):
        result = Board().show_board(["0", "1", "2", "3", "4", "5", "6", "7", "8"])
        expected = " 0 | 1 | 2 \n===+===+===\n 3 | 4 | 5 \n===+===+===\n 6 | 7 | 8 \n"
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
