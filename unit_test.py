import unittest

from flatten import Flatten


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


if __name__ == '__main__':
    unittest.main()
