from machine import Pin
from dht import DHT11

from hardware.sensors.sensor import AbstractSensor
from utils import convert_temperature, convert_humidity

class DHT(AbstractSensor):
    def __init__(self, device, pin: int) -> None:
        super().__init__(device)
        self.sensor = DHT11(Pin(pin, Pin.IN))

    def get_measurements(self) -> dict:
        self.sensor.measure()

        temperature = convert_temperature(self.sensor.temperature(), self.device.settings.temperature_units)
        humidity = convert_humidity(self.sensor.temperature(), self.sensor.humidity(),
                                    self.device.settings.humidity_units)
        measurements = {'temperature': {'value': temperature, 'units': self.device.settings.temperature_units},
                        'humidity': {'value': humidity, 'units': self.device.settings.humidity_units}}

        return measurements

    def check_measurements(self) -> bool:
        self.sensor.measure()

        if not (0 <= self.sensor.temperature() <= 50 and 20 <= self.sensor.humidity() <= 95):
            return False

        return True