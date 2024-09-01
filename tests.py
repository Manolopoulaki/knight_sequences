import unittest
from main import is_valid, count_sequences, total_valid_sequences, keypad, vowels, knight_moves

class TestKeypadSequences(unittest.TestCase):

    def test_is_valid(self):
        self.assertTrue(is_valid(0, 0))  # 'A'
        self.assertTrue(is_valid(3, 1))  # '1'
        self.assertFalse(is_valid(3, 0))  # None
        self.assertFalse(is_valid(4, 0))  # Out of bounds

    def test_count_sequences(self):
        
        # Test starting from '2', which should have more than 1 moves
        self.assertGreater(count_sequences(3, 2, 1, 0), 1)
        
        # Test a case where we've used more than 2 vowels
        self.assertEqual(count_sequences(0, 0, 1, 3), 0)

    def test_total_valid_sequences(self):
        # We don't know the exact number, but it should be positive
        self.assertGreater(total_valid_sequences(), 0)
        
        # The result should be an integer
        self.assertIsInstance(total_valid_sequences(), int)

    def test_keypad_structure(self):
        self.assertEqual(len(keypad), 4)
        self.assertEqual(len(keypad[0]), 5)
        self.assertIsNone(keypad[3][0])
        self.assertIsNone(keypad[3][4])

    def test_vowels(self):
        self.assertEqual(vowels, {'A', 'E', 'I', 'O'})

    def test_knight_moves(self):
        expected_moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        self.assertEqual(set(knight_moves), set(expected_moves))

if __name__ == '__main__':
    unittest.main()