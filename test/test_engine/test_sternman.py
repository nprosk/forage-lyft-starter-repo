import unittest

from engine.sternman_engine import SternmanEngine

class TestSternman(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light_on = True

        engine = SternmanEngine(warning_light_on)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        warning_light_on = False

        engine = SternmanEngine(warning_light_on)
        self.assertFalse(engine.needs_service())