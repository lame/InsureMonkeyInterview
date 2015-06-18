import unittest

from flatten import Flatten
from csv import CommaSeparatedValues


class Test_Scripts(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_flatten(self):
        self.assertEqual(Flatten.flatten_list([['a', 'b'], ['c', ['d', 'e', ], ['f'], 'g']]),
                         ['a', 'b', 'c', 'd', 'e', 'f', 'g'])
        self.assertEqual(Flatten.flatten_list([['a', 'b'], 'a', ['a', 'b', ], ['a'], 'b']),
                         ['a', 'b', 'a', 'a', 'b', 'a', 'b'])

    def test_comma_separated_values(self):
        self.assertEqual(CommaSeparatedValues(3456).output, '3,456')
        self.assertEqual(CommaSeparatedValues(987654321).output, '987,654,321')
        self.assertEqual(CommaSeparatedValues(20).output, '20')
        self.assertEqual(CommaSeparatedValues(12.3).output, '12.3')
        self.assertEqual(CommaSeparatedValues(3456.3).output,  '3,456.3')

if __name__ == '__main__':
    unittest.main()
