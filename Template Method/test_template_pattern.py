import os
import unittest

from .foo import FileAverageCalculator, AverageCalculator

setup_done = False


class TemplatePatternTest(unittest.TestCase):
    def setUp(self):
        self.file_data = [1, 2, 3, 4, 5]

        with open('test_file.txt', 'a') as test_file:
            for data in self.file_data:
                test_file.write(str(data) + "\n")

        self.file = open('./test_file.txt')

    def test_is_sub_class(self):
        self.assertTrue(issubclass(FileAverageCalculator, AverageCalculator))

    def test_result(self):
        fac = FileAverageCalculator(self.file)
        self.assertEqual(fac.average(),
                         sum(self.file_data) / len(self.file_data))

    def tearDown(self):
        os.remove('test_file.txt')
