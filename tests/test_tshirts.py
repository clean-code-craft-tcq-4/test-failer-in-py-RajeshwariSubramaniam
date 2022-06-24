from unittest import TestCase
from inspect import signature

from src import tshirts


class TestTshirts(TestCase):

    def test_tshirts_size(self):
        actual_parameter = signature(tshirts.size)
        self.assertEqual(len(actual_parameter.parameters), 2)
