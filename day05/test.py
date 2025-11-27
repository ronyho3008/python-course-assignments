import unittest
import word_scramble as game


class TestWordScramble(unittest.TestCase):
    def test_scramble_word_changes_order(self):
        word = "protein"
        scrambled = game.scramble_word(word)
        self.assertEqual(sorted(scrambled), sorted(word))
        self.assertNotEqual(scrambled, word) # usually — random can match occasionally
    
    def test_scramble_word_same_letters(self):
        word = "aaaaa"
        scrambled = game.scramble_word(word)
        self.assertEqual(scrambled, word)

    def test_word_list_not_empty(self):
        self.assertTrue(len(game.WORDS) > 0)

    def test_scrambled_length(self):
        for word in game.WORDS:
            scrambled = game.scramble_word(word)
            self.assertEqual(len(scrambled), len(word))

if __name__ == '__main__':
    unittest.main()