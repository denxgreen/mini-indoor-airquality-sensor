def convert_temperature(value: int, units: str) -> float:
    if units == TempUnit.METRIC:
        return value
    if units == TempUnit.IMPERIAL:
        return value * 9/5 + 32
    if units == TempUnit.STANDARD:
        return value + 273.15
    
    raise ValueError(f'Unit "{units}" is invalid.')

class TemperatureUnit:
    IMPERIAL: str = "imperial"
    STANDARD: str = "standard"
    METRIC: str = "metric"