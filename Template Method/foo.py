# Abstract Base Class Imports
from abc import ABC, abstractclassmethod


class AverageCalculator(ABC):
    """
        Average Calculator for Any Data Structure. Template Method/
        Class inheriting this class must implement abstract methods
    """

    # noqa
    def average(self):
        try:
            num_items = 0
            total_sum = 0
            while self.has_next():
                total_sum += self.next_item()
                num_items += 1
            if num_items == 0:
                raise RuntimeError("Cannot Compute average")
            return total_sum / num_items
        finally:
            self.dispose()

    @abstractclassmethod
    def has_next(self):
        pass

    @abstractclassmethod
    def next_item(self):
        pass

    def dispose(self):
        pass


class FileAverageCalcularor(AverageCalculator):
    """Calculates the average of the numbers on each line"""

    # noqa
    def __init__(self, file):
        self.file = file
        self.last_line = self.file.readline()

    def has_next(self):
        return self.last_line != ''

    def next_item(self):
        result = float(self.last_line)
        self.last_line = self.file.readline()
        return result

    def dispose(self):
        self.file.close()