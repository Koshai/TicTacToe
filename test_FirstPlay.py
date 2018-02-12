import unittest

from FirstPlay import FirstPlay

class ChooseYorN(unittest.TestCase):

    def test_chooseY(self):
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda : "Y"
        self.assertEqual(FirstPlay().first_play(), "Y")
        __builtins__.raw_input = original_raw_input

    def test_chooseN(self):
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda : "N"
        self.assertEqual(FirstPlay().first_play(), "N")
        __builtins__.raw_input = original_raw_input

if __name__ == '__main__':
    unittest.main()