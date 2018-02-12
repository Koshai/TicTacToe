import unittest

from GameSelection import GameSelection

class ChooseOne(unittest.TestCase):

    def test_choose1(self):
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda : 1
        self.assertEqual(GameSelection().game_selection(), 1)
        __builtins__.raw_input = original_raw_input

    def test_choose2(self):
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda : 2
        self.assertEqual(GameSelection().game_selection(), 2)
        __builtins__.raw_input = original_raw_input

    def test_choose3(self):
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda: 3
        self.assertEqual(GameSelection().game_selection(), 3)
        __builtins__.raw_input = original_raw_input

if __name__ == '__main__':
    unittest.main()