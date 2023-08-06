import unittest
from pylogex import regex
import logging

logging.basicConfig(level=logging.INFO)

"""
To run all test files starting with test_ in tests/ directory,
run command: python3 -m unittest discover -s tests
"""

class TestRegex(unittest.TestCase):

    def test_regex_matcher_valid_input(self):
        """
        Test regex_matcher function for a valid input
        """
        s = 'news/100'
        pattern = '(?P<resource>\w+)/(?P<id>\d+)'
        output_list=regex.regex_matcher(s,pattern)
        self.assertEqual(output_list[0]["resource"], "news")
        self.assertEqual(output_list[0]["id"], "100")

    def test_regex_matcher_no_match(self):
        """
        Test regex_matcher function for no matches found
        """
        s = 'news/100'
        pattern = '123'
        output_list=regex.regex_matcher(s,pattern)
        logging.info(output_list)
        self.assertEqual(output_list, [])

    def test_regex_matcher_invalid_input(self):
        """
        Test regex_matcher function for invalid input
        """
        s = 123
        pattern = 123
        with self.assertRaises(TypeError):
            output_list=regex.regex_matcher(s,pattern)
            self.assertEqual(output_list, [])

if __name__ == '__main__':
    unittest.main()