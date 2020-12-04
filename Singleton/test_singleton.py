import unittest
from .foo import Foo


class SingletonTest(unittest.TestCase):
    # noqa

    def setUp(self):
        self.instance1 = Foo()
        self.instance2 = Foo()

    def test_has_same_id(self):
        """Test if the instance have same identity"""
        self.assertNotEqual(id(self.instance1), id(self.instance2))

    def test_is_instance_of_same_class(self):
        """Test if both instance are of same class"""
        self.assertEqual(self.instance1.__class__, self.instance2.__class__)

    def test_is_equal(self):
        """Test if both instance are equal"""
        self.assertEqual(self.instance1, self.instance2)
