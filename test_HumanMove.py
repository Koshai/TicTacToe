import unittest
import sys

from HumanMove import HumanMove

class ChooseYorN(unittest.TestCase):

    def test_choose0(self):
        player = "Y"
        board = ["0", "1", "2", "3", "Y", "5", "6", "7", "8"]

        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda : 0
        self.assertEqual(HumanMove().get_human_spot(player, board), 'Taken')
        __builtins__.raw_input = original_raw_input

if __name__ == '__main__':
    unittest.main()