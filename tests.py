import unittest
from util import algorithm, re_algorightm


class AlgorithmTester(unittest.TestCase):

    def test_algorithm_on_first_data_example(self):
        self.assertEqual(algorithm('in1.txt'), re_algorightm('in1.txt'))

    def test_algorithm_on_second_data_example(self):
        self.assertEqual(algorithm('in2.txt'), re_algorightm('in2.txt'))

    def test_algorithm_on_third_data_example(self):
        self.assertEqual(algorithm('in3.txt'), re_algorightm('in3.txt'))


if __name__ == '__main__':
    unittest.main()
