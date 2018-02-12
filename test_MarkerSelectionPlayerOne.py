import unittest

from MarkerSelectionPlayerOne import MarkerSelectionPlayerOne

class ChooseYorN(unittest.TestCase):

    def test_choose1(self):
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda : "A"
        self.assertEqual(MarkerSelectionPlayerOne().select_marker(), "A")
        __builtins__.raw_input = original_raw_input

if __name__ == '__main__':
    unittest.main()