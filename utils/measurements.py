from math import exp
import json

from constants import MEASUREMENTS_FILE

class HumidityUnit:
    ABSOLUTE: str = "absolute"
    RELATIVE: str = "relative"

class TemperatureUnit:
    IMPERIAL: str = "imperial"
    STANDARD: str = "standard"
    METRIC: str = "metric"

def read_measurements() -> dict:
    with open(MEASUREMENTS_FILE, 'r') as file:
        measurements = json.load(file)
        return measurements

def write_measurements(measurements: dict) -> None:
    with open(MEASUREMENTS_FILE, 'w') as file:
        json.dump(measurements, file)

def convert_temperature(temperature: int, units: str) -> float:
    if units == TemperatureUnit.METRIC:
        return temperature
    if units == TemperatureUnit.IMPERIAL:
        return temperature * 9 / 5 + 32
    if units == TemperatureUnit.STANDARD:
        return temperature + 273.15

    raise ValueError(f'Unit "{units}" is invalid.')

def convert_humidity(temperature: int, humidity: int, units: str) -> float:
    if units == HumidityUnit.RELATIVE:
        return humidity
    if units == HumidityUnit.ABSOLUTE:
        saturation_vapor_pressure = 6.112 * exp((17.67 * temperature) / (temperature + 243.5))
        actual_vapor_pressure = (humidity / 100) * saturation_vapor_pressure
        return (216.7 * actual_vapor_pressure) / (temperature + 273.15)