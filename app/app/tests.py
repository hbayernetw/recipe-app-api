"""
Sample Test
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc mocule."""

    def test_add_numbers(self):
        """Tests adding numbers together"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Test subtracting numbers"""
        res = calc.subtract(5, 6)

        self.assertEqual(res, -1)
