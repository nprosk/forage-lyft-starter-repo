import unittest

from tire.carrigan_tire import CarriganTire

class TestCarrigan(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tire = CarriganTire([0.9, 0.6, 0.8, 0.7])
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        tire = CarriganTire([0.8, 0.8, 0.8, 0.1])
        self.assertFalse(tire.needs_service())