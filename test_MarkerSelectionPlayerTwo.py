import unittest

from MarkerSelectionPlayerTwo import MarkerSelectionPlayerTwo

class ChooseYorN(unittest.TestCase):

    def test_choose1(self):
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda : "B"
        self.assertEqual(MarkerSelectionPlayerTwo().select_marker(), "B")
        __builtins__.raw_input = original_raw_input

if __name__ == '__main__':
    unittest.main()