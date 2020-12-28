import unittest
from util import algorithm


class AlgorithmTester(unittest.TestCase):

    def test_algorithm_on_first_data_example(self):
        self.assertEqual(algorithm('in1.txt'), [0, 1, 2, 3, 16, 17])

    def test_algorithm_on_second_data_example(self):
        self.assertEqual(algorithm('in2.txt'), [2, 4, 13, 16, 20])

    def test_algorithm_on_third_data_example(self):
        self.assertEqual(algorithm('in3.txt'), [14, 16, 22])

    def test_algorithm_on_fourth_data_example(self):
        self.assertEqual(algorithm('in4.txt'), [0, 7, 32])


if __name__ == '__main__':
    unittest.main()
