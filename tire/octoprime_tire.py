from abc import ABC
from tire.tire import Tire

class OctoprimeTire(Tire, ABC):
    def __init__(self, sensors):
        self.sensors = sensors
    
    def needs_service(self):
        return sum(self.sensors) >= 3