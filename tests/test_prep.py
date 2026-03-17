import unittest
from prep import strange_function


class MyTestCase(unittest.TestCase):

    def test_strange_function1(self):
        self.assertEqual(
            strange_function(1, 2, 3, 4),
            'behaviour 3'
        )

    def test_behaviour_1(self):
        self.assertEqual(
            strange_function(1, 1, 2, 3),
            'behaviour 1'
        )

    def test_behaviour_2(self):
        self.assertEqual(
            strange_function(1, 1, 5, 3),
            'behaviour 2'
        )

    def test_behaviour_4(self):
        self.assertEqual(
            strange_function(5, 4, 3, 2),
            'behaviour 4'
        )

    def test_behaviour_5(self):
        self.assertEqual(
            strange_function(5, 4, 3, 4),
            'behaviour 5'
        )

    def test_behaviour_6(self):
        self.assertEqual(
            strange_function(3, 4, 3, 4),
            'behaviour 6'
        )


if __name__ == '__main__':
    unittest.main()