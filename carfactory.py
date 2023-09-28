from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire
from car import Car

class CarFactory():
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_sensor):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTire(tire_sensor)
        return Car(engine, battery, tires)
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_sensor):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = OctoprimeTire(tire_sensor)
        return Car(engine, battery, tires)
    def create_palindrome(current_date, last_service_date, warning_light_on, tire_sensor):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTire(tire_sensor)
        return Car(engine, battery, tires)
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_sensor):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = OctoprimeTire(tire_sensor)
        return Car(engine, battery, tires)
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_sensor):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = CarriganTire(tire_sensor)
        return Car(engine, battery, tires)