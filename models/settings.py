from models.udataclasses import BaseModel, validator
from utils.measurements import TemperatureUnit, HumidityUnit
from utils.errors import SettingsError

class Settings(BaseModel):
    temperature_units: str = TemperatureUnit.STANDARD
    humidity_units: str = HumidityUnit.RELATIVE

    @validator('temperature_units')
    def check_temperature_units(self, value: str) -> None:
        if value not in (TemperatureUnit.METRIC, TemperatureUnit.STANDARD, TemperatureUnit.IMPERIAL):
            raise SettingsError(f'Temperature unit "{value}" is invalid.')

    @validator('humidity_units')
    def check_humidity_units(self, value: str) -> None:
        if value not in (HumidityUnit.ABSOLUTE, HumidityUnit.RELATIVE):
            raise SettingsError(f'Humidity unit "{value}" is invalid.')