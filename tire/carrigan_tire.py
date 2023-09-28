from abc import ABC
from tire.tire import Tire

class CarriganTire(Tire, ABC):
    def __init__(self, sensors):
        self.sensors = sensors

    def needs_service(self):
        for val in self.sensors:
            if val >= 0.9:
                return True
        return False