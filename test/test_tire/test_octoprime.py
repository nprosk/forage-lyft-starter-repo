import unittest

from tire.octoprime_tire import OctoprimeTire

class TestOctoprime(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tire = OctoprimeTire([0.9, 0.2, 0.1, 0.3])
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        tire = OctoprimeTire([0.8, 0.8, 0.8, 0.8])
        self.assertFalse(tire.needs_service())