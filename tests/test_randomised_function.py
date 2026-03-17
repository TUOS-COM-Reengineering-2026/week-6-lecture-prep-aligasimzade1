import unittest
from unittest.mock import patch
from lecture import randomised_function


class MyTestCase(unittest.TestCase):

    @patch("lecture.randint", return_value=3)
    def test_randomised_function(self, mock_randint):
        self.assertEqual('software', randomised_function())