# Science Word Scramble — README

## English

### Installation

This game has **no external dependencies**. It uses only Python's built-in libraries.
Make sure you have **Python 3.8+** installed.

### How to Run the Game

1. Download `science_word_scramble.py`.
2. Open a terminal in the file's folder.
3. Run:

```bash
python science_word_scramble.py
```

4. Follow the instructions in the terminal.

### Running the Tests

1. Save the test file as `test_science_scramble.py`.
2. Run:

```bash
python -m unittest test_science_scramble.py
```

---

## עברית

### התקנה

למשחק **אין ספריות חיצוניות**. הוא משתמש רק בספריות שמגיעות עם פייתון.
יש לוודא כי מותקן במחשב **Python 3.8 ומעלה**.

### איך מריצים את המשחק

1. הורידי את הקובץ `science_word_scramble.py`.
2. פתחי חלון טרמינל בתיקייה שבה נמצא הקובץ.
3. הריצי:

```bash
python science_word_scramble.py
```

4. עקבי אחר ההנחיות במסך.

### הרצת בדיקות

1. שמרי את קובץ הבדיקות בשם `test_science_scramble.py`.
2. הריצי:

```bash
python -m unittest test_science_scramble.py
```

---

# Tests (test_science_scramble.py)

```python
import unittest
import science_word_scramble as game

class TestWordScramble(unittest.TestCase):

    def test_scramble_word_changes_order(self):
        word = "protein"
        scrambled = game.scramble_word(word)
        self.assertEqual(sorted(scrambled), sorted(word))
        self.assertNotEqual(scrambled, word)  # usually — random can match occasionally

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
```
