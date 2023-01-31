import unittest
from lezione7 import somma

class TestSomma(unittest.TestCase):
    def test_somma(self):
        self.assertEqual(somma(1,6), 7)


if __name__ == "__main__":
    unittest.main()