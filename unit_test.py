import unittest

from datetime import date
from scripts import CommaSeparatedValues, FlattenList, GetNextDate


class Test_Scripts(unittest.TestCase):

    def setUp(self):
        self.comma_test = CommaSeparatedValues()
        self.next_date_test = GetNextDate()

    def tearDown(self):
        pass

    def test_flatten(self):
        self.assertEqual(FlattenList.flatten([['a', 'b'], ['c', ['d', 'e', ], ['f'], 'g']]),
                         ['a', 'b', 'c', 'd', 'e', 'f', 'g'])
        self.assertEqual(FlattenList.flatten([['a', 'b'], 'a', ['a', 'b', ], ['a'], 'b']),
                         ['a', 'b', 'a', 'a', 'b', 'a', 'b'])

    def test_comma_separated_values(self):
        self.assertEqual(self.comma_test.comma_separated_numbers(3456), '3,456')
        self.assertEqual(self.comma_test.comma_separated_numbers(987654321), '987,654,321')
        self.assertEqual(self.comma_test.comma_separated_numbers(20), '20')
        self.assertEqual(self.comma_test.comma_separated_numbers(12.3), '12.3')
        self.assertEqual(self.comma_test.comma_separated_numbers(3456.3),  '3,456.3')

    def test_get_next_date(self):
        self.assertEqual(self.next_date_test.get_next_dates(date(2014, 5, 1), 2, 1, 0),
                         [date(2014, 6, 1), date(2014, 7, 1)])
        self.assertEqual(self.next_date_test.get_next_dates(date(2014, 5, 2), 3, 0, 3),
                         [date(2014, 5, 2), date(2014, 6, 1), date(2014, 7, 1)])
        self.assertEqual(self.next_date_test.get_next_dates(date(2014, 5, 10), 3, 0, 3),
                         [date(2014, 6, 1), date(2014, 7, 1), date(2014, 8, 1)])
        self.assertEqual(self.next_date_test.get_next_dates(date(2014, 5, 30), 3, 1, -3),
                         [date(2014, 7, 3), date(2014, 8, 1), date(2014, 9, 1)])

if __name__ == '__main__':
    unittest.main()
